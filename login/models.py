from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RegisterUser(User):
    emailuser=models.CharField(max_length=100)