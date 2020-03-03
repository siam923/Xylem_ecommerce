from django.contrib.auth.models import AbstractUser
from django.db import models

#signals
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# User model
class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    brand = models.CharField(max_length=10, verbose_name='Brand Name')
    info = models.CharField(max_length=255, verbose_name='Brand Info')

    def __str__(self):
        return f"{self.user.username}:{self.brand}"

    # @receiver(post_save, sender=CustomUser)
    # def create_user_profile(self, sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=CustomUser)
    # def save_user_profile(self, sender, instance, **kwargs):
    #     instance.profile.save()
