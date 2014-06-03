from django.contrib.auth.models import User
from django import forms
from crm.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email','username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description',)
