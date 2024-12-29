from django.contrib.auth.models import User
from django.db import models


# Model for Nutritionist
class Nutritionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email


# Model for UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    nutritionist = models.ForeignKey(
        Nutritionist, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.email
