from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class RegistroForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    