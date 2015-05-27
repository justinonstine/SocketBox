__author__ = 'justinonstine'
from django import forms
from django.contrib.auth.models import User
from socketbox.models import UserProfile, Location

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phoneNumber',)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('address', 'city', 'state')