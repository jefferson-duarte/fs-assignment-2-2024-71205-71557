from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Nutritionist, UserProfile


# Serializer for registering a nutritionist
class NutritionistRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    registration_number = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'registration_number',
            'email', 'phone', 'password', 'confirm_password'
        ]

    def validate(self, data):
        # Ensure passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."}
            )

        # Check if email already exists
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )

        # Remove confirm_password from the data dictionary
        data.pop('confirm_password')

        return data

    def create(self, validated_data):
        # Remove the password from the validated data
        password = validated_data.pop('password')
        # Get the phone number
        phone = validated_data.pop('phone')
        # Get the registration number
        registration_number = validated_data.pop('registration_number')
        # Hash the password
        validated_data['password'] = make_password(password)
        # Generate a unique username based on the email
        email = validated_data['email']
        # Use the part before "@" in the email as the username
        username = email.split('@')[0]

        validated_data['username'] = username
        # Create the nutritionist with the hashed password
        nutritionist = User.objects.create(**validated_data)

        # Create the nutritionist profile and save the phone and registration number  # noqa: E501
        Nutritionist.objects.create(
            user=nutritionist,
            phone=phone,
            registration_number=registration_number
        )

        return nutritionist


# View for registering a nutritionist
class NutritionistRegisterView(generics.CreateAPIView):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistRegisterSerializer


# Serializer for registering a user (client)
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
        # Ensure passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."}
            )

        # Check if email already exists
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )

        # Remove confirm_password from the data dictionary
        data.pop('confirm_password')

        return data

    def create(self, validated_data):
        # Remove the password from the validated data
        password = validated_data.pop('password')
        # Get the phone number
        phone = validated_data.pop('phone')
        # Hash the password
        validated_data['password'] = make_password(password)
        # Generate a unique username based on the email
        email = validated_data['email']
        # Use the part before "@" in the email as the username
        username = email.split('@')[0]

        validated_data['username'] = username

        # Create the user with the hashed password
        user = User.objects.create(**validated_data)

        # Create the user profile and save the phone number
        UserProfile.objects.create(user=user, phone=phone)

        return user


# View for registering a user (client)
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# Custom token serializer to add extra claims
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.first_name + " " + user.last_name
        return token


# Custom view to use the custom token serializer
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
