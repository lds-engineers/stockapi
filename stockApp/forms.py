from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

# class LoginForm(AuthenticationForm):
#     username = UsernameField(
#         widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
#     )
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(attrs={"class": "form-control"}),
#     )
    
class customerRegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
