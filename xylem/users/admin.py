from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, VendorProfile
#from .forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.register(CustomUser)
admin.site.register(VendorProfile)
