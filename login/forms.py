import imp
from django.forms import ModelForm

from login.models import RegisterUser
class RegisterUserForm(ModelForm):
    class Meta:
        model=RegisterUser
        fields=['first_name','last_name','username','password','role','address','state','pincode','city','profile_picture']