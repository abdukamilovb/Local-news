from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    lavozimi = models.CharField(max_length=100, blank=True, null=True)  # Yangi ustun qo‘shildi

    

    def __str__(self):
        return f"{self.username} ({self.lavozimi if self.lavozimi else 'Lavozimi yo‘q'})"
