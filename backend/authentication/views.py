from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, views
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from .models import Nutritionist, UserProfile
from .serializers import (ClientSerializer, NutritionistListSerializer,
                          NutritionistProfileSerializer,
                          NutritionistRegisterSerializer,
                          UserProfileSerializer, UserRegisterSerializer)


# Custom permission to check if the user is a client (i.e., has a user profile)
class IsClientUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'userprofile') and request.user.userprofile is not None  # noqa:E501


# View to list available nutritionists for clients
class AvailableNutritionistsView(generics.ListAPIView):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistListSerializer
    permission_classes = [IsAuthenticated, IsClientUser]


# View to allow clients to select a nutritionist
class SelectNutritionistView(views.APIView):
    permission_classes = [IsAuthenticated, IsClientUser]

    def post(self, request):
        user_profile = request.user.userprofile
        nutritionist_id = request.data.get('nutritionist_id')
        nutritionist = get_object_or_404(Nutritionist, id=nutritionist_id)
        user_profile.nutritionist = nutritionist
        user_profile.save()
        return Response({"message": "Nutritionist selected successfully"})


# View to get the profile of the authenticated user (client or nutritionist)
class UserProfileView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if hasattr(request.user, 'userprofile'):
            user_profile = get_object_or_404(UserProfile, user=request.user)
            serializer = UserProfileSerializer(user_profile)
        elif hasattr(request.user, 'nutritionist'):
            nutritionist_profile = get_object_or_404(Nutritionist, user=request.user)  # noqa:E501
            serializer = NutritionistProfileSerializer(nutritionist_profile)
        return Response(serializer.data)


# View for registering a nutritionist
class NutritionistRegisterView(generics.CreateAPIView):
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistRegisterSerializer


# View for registering a user (client)
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Use the custom user model
    serializer_class = UserRegisterSerializer


class ClientsOfNutritionistView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if hasattr(request.user, 'nutritionist'):
            nutritionist = request.user.nutritionist
            clients = get_list_or_404(UserProfile, nutritionist=nutritionist)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        return Response({"error": "User is not a nutritionist"}, status=403)
