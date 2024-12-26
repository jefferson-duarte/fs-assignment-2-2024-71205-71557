from django.contrib import admin

from .models import Nutritionist


@admin.register(Nutritionist)
class NutritionistAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'registration_number', 'email', 'phone'
    ]
