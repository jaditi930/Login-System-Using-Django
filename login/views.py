from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import RegisterUser
# Create your views here.
def index(request):
    return render(request,"index.html")

def signup_user(request):
    username=request.POST["name"]
    password=request.POST["password"]
    new_user=RegisterUser.objects.create(username=username,password=password,emailuser="aditi")
    new_user.save()
    return render(request,"signup_user.html",context={"name":username})