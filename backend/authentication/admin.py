from django.contrib import admin

from .models import Nutritionist, UserProfile


@admin.register(Nutritionist)
class NutritionistAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'registration_number', 'phone',
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'phone',
    ]
