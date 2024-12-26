import random

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Nutritionist, UserProfile


# Serializador para registrar nutricionista
class NutritionistRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Nutritionist
        fields = [
            'name', 'registration_number', 'email',
            'phone', 'password', 'confirm_password'
        ]

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords must match.")

        # Remover confirm_password do dicionário antes de criar o usuário
        data.pop('confirm_password')

        return data

    def create(self, validated_data):
        # Remover a senha do dicionário
        password = validated_data.pop('password')
        # Criptografar a senha
        validated_data['password'] = make_password(password)
        # Criar o nutricionista com a senha criptografada
        nutritionist = Nutritionist.objects.create(**validated_data)

        return nutritionist


# View para registro de nutricionista
class NutritionistRegisterView(generics.CreateAPIView):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistRegisterSerializer


# Serializador para registrar usuário (cliente)
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email',
            'phone', 'password', 'confirm_password'
        ]

    def validate(self, data):
        # Verifica se o email já existe
        if User.objects.filter(email=data['email']).exists():
            raise ValidationError("A user with this email already exists.")

        # Remover confirm_password do dicionário antes de salvar o usuário
        data.pop('confirm_password')

        return data

    def create(self, validated_data):
        # Remove a senha do dicionário
        password = validated_data.pop('password')
        # Pega o telefone
        phone = validated_data.pop('phone')
        # Criptografa a senha
        validated_data['password'] = make_password(password)
        # Gerar um username único com base no email
        email = validated_data['email']
        # Usa a parte antes do "@" no email como username
        username = email.split('@')[0]

        # Garantir que o username seja único
        while User.objects.filter(username=username).exists():
            # Adiciona um número aleatório para garantir unicidade
            username = f"{username}{random.randint(1, 100)}"

        validated_data['username'] = username
        # Cria o usuário com a senha criptografada
        user = User.objects.create(**validated_data)
        # Cria o perfil de usuário e salva o telefone

        UserProfile.objects.create(user=user, phone=phone)

        return user


# View para registro de usuário (cliente)
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# View para login (autenticação)
class LoginView(APIView):
    """
    View to handle user login using email and password and return a JWT token if the credentials are valid.
    """  # noqa:E501

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        # Verifica se email e senha foram fornecidos
        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)  # noqa:E501

        # Tenta autenticar o usuário usando email
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Usuário autenticado, gera o token JWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Retorna o token JWT
            return Response({
                "access": access_token,
                "refresh": str(refresh)
            })

        # Se as credenciais estiverem incorretas
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)  # noqa:E501


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None
        return None
