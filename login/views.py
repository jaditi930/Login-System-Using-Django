from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RegisterUser
from .forms import RegisterUserForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")
def signin(request):
    form=RegisterUserForm()
    return render(request,"sign_in.html",{"form":form})
def log_user(request):
    return render(request,"login.html")

def authenticate_user(request):
    username=request.POST["name"]
    password=request.POST["password"]
    user=RegisterUser.objects.get(username=username)
    user.check_password(password)
    if user is not None:
        login(request,user)
        return render(request,"user_details.html",{"user":user})
    else:
        return redirect("/")
def logout_user(request):
    logout(request)
    return redirect("/")
def signup_user(request):
    new_form=RegisterUserForm(request.POST or None, request.FILES or None)
    try:
        new_form.save()
        this_user=RegisterUser.objects.get(username=new_form.cleaned_data['username'])
        this_user.set_password(new_form.cleaned_data['password'])
        print(this_user.password)
        return render(request,"login.html")
    except:
        return redirect("/signin/")
