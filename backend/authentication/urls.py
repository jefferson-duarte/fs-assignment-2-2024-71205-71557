from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import auth_jwt, views

urlpatterns = [
    # URL pattern for user registration
    path(
        'api/register/user/', views.UserRegisterView.as_view(), name='register_user'  # noqa:E501
    ),
    # URL pattern for nutritionist registration
    path(
        'api/register/nutritionist/', views.NutritionistRegisterView.as_view(), name='register_nutritionist'  # noqa:E501
    ),
    # URL pattern for obtaining JWT token
    path(
        'api/token/', auth_jwt.MyTokenObtainPairView.as_view(), name='token_obtain_pair'  # noqa:E501
    ),
    # URL pattern for refreshing JWT token
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    # URL pattern for verifying JWT token
    path(
        'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'
    ),

    # URL pattern for listing all nutritionists
    path(
        'api/nutritionists/', views.AvailableNutritionistsView.as_view(), name='nutritionists'  # noqa:E501
    ),
    # URL pattern for selecting a nutritionist
    path(
        'api/select-nutritionist/', views.SelectNutritionistView.as_view(), name='select_nutritionist'  # noqa:E501
    ),
    # URL pattern for getting user profile
    path(
        'api/user-profile/', views.UserProfileView.as_view(), name='user_profile'  # noqa:E501
    ),
]
