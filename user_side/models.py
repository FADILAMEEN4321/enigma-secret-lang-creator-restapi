from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=False)
    is_verified = models.BooleanField(default=False, blank=True, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"