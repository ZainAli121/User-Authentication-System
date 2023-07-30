from django.contrib import admin
from django.urls import path, include
from userauthapp import views

urlpatterns = [
    path('', views.blog, name='name'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('blog', views.blog, name='blog'),
    path('signup', views.signupuser, name='signup')
]
