# authentication/forms.py
from django import forms
from .models import UserProfile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'company_name', 'phone_number', 'business_email', 'password']

class LoginForm(forms.Form):
    business_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
