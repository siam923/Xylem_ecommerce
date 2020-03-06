from django.contrib import admin
from .models import Cart, Order
#from .forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.register(Cart)
admin.site.register(Order)
