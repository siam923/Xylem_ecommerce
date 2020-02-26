from django.contrib.auth.models import AbstractUser
from django.db import models


# User model
class CustomUser(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=False, null=False)

# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.user.first_name

class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    shop = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.shop
