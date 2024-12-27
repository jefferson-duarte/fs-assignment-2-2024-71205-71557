from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import (MyTokenObtainPairView, NutritionistRegisterView,
                    UserRegisterView)

urlpatterns = [
    # URL pattern for user registration
    path(
        'api/register/user/', UserRegisterView.as_view(), name='register_user'
    ),
    # URL pattern for nutritionist registration
    path(
        'api/register/nutritionist/', NutritionistRegisterView.as_view(), name='register_nutritionist'  # noqa:E501
    ),
    # URL pattern for obtaining JWT token
    path(
        'api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    # URL pattern for refreshing JWT token
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    # URL pattern for verifying JWT token
    path(
        'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'
    ),
]
