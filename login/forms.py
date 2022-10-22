import imp
from django.forms import ModelForm

from login.models import RegisterUser
from django.forms import TextInput
class RegisterUserForm(ModelForm):
    class Meta:
        model=RegisterUser
        fields=['first_name','last_name','username','password','email','role','address','state','pincode','city','profile_picture']
        widgets={
            'password': TextInput(attrs={'type': 'password'}),
        }