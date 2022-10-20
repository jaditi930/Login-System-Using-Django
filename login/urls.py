from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('signup_user/',views.signup_user),
    path('logged_user/',views.log_user),
    path('logged_user/user_authenticate/',views.authenticate_user),
    path('logged_user/user_authenticate/logout/',views.logout_user),
]
