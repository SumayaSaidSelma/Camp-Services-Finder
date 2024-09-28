from django import forms
from .models import Service  # Import the Service model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for creating and updating services
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'category', 'location', 'description', 'contact_info', 'hours']  # Fields to display in the form
