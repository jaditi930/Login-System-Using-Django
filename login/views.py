from django.shortcuts import render,redirect
from django.http import HttpResponse
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
        return render(request,"user_details.html",{"user":user})
    else:
        return HttpResponse("Not found")
def logout_user(request):
    logout(request)
    return redirect("/")
def signup_user(request):
    username=request.POST["name"]
    password=request.POST["password"]
    profile_picture=request.FILES["photo"]
    exis_user=RegisterUser.objects.get(username=username)
    print(exis_user)
    if exis_user is None:
        new_user=RegisterUser.objects.create(username=username,password=password,profile_picture=profile_picture)
        new_user.set_password(password)
        new_user.save()
        return render(request,"login.html")
    else:
        return HttpResponse("User Already Exists!Try Again!")
