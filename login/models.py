from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
role_choices=(("Patient","Patient"),("Doctor","Doctor"))
class RegisterUser(User):
    profile_picture=models.ImageField(null=True)
    address=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    pincode=models.BigIntegerField(null=True)
    role=models.CharField(max_length=200,choices=role_choices,default="Patient")
