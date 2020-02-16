from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Customer, Vendor



admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Vendor)
