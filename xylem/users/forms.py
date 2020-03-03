from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#from django.db import transaction # allows to save additional info-> see doc
# Importing users
from django.contrib.auth import get_user_model
#from .models import (Vendor, Customer)
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm): 
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField(max_length=255, label='Address')
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20, label='Last Name')

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.
        user.gender = self.cleaned_data['gender']
        user.address = self.cleaned_data['address']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        # You must return the original result.
        return user
