from django.urls import path

from .views import LoginView, NutritionistRegisterView, UserRegisterView

urlpatterns = [
    path(
        'api/register/user/', UserRegisterView.as_view(), name='register_user'
    ),
    path(
        'api/register/nutritionist/', NutritionistRegisterView.as_view(), name='register_nutritionist'  # noqa:E501
    ),
    path('api/login/', LoginView.as_view(), name='login'),
]
