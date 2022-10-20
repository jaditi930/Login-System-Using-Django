from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RegisterUser(User):
    profile_picture=models.ImageField(upload_to="user_profiles",null=True)