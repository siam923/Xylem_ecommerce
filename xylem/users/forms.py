from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.db import transaction # allows to save additional info-> see doc
# Importing users
from django.contrib.auth import get_user_model
from .models import (Vendor, Customer)


class CustomerSignUpForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(required=True, label='Sex', choices=GENDER_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'address', 'first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        gender = self.cleaned_data.get('gender')
        customer = Customer.objects.create(user=user, gender=gender)
        return user


class VendorSignUpForm(UserCreationForm):
    shop = forms.CharField(label='Shop Name')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'address', 'first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True

        user.save()
        shop = self.cleaned_data.get('shop')
        customer = Vendor.objects.create(user=user, shop=shop)

        return user
