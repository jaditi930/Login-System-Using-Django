from django.shortcuts import render
from django.http import Http404, HttpResponse,JsonResponse
from .models import RegisterUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")
def signin(request):
    return render(request,"sign_in.html")
def log_user(request):
    return render(request,"login.html")

def authenticate_user(request):
    username=request.POST["name"]
    password=request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request,"user_details.html")
    else:
        return HttpResponse("Not found")
def logout_user(request):
    logout(request)
    return render(request,"index.html")
def signup_user(request):
    username=request.POST["name"]
    password=request.POST["password"]
    profile_picture=request.FILES["photo"]
    new_user=RegisterUser.objects.create(username=username,password=password,profile_picture=profile_picture)
    new_user.set_password(password)
    new_user.save()

    return render(request,"login.html")