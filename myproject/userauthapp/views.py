from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from userauthapp.models import Signup
from django.contrib import messages

# Create your views here.
def blog(request):
    if request.user.is_anonymous:
        messages.error(request, "Please sign in to continue")
        return redirect("/login")
    return render(request, 'blog.html')

def loginuser(request):
    if request.method == 'POST':
        # Check if user enters correct credentials
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return render(request, 'login.html')
            
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect("/login")

def signupuser(request):
    if request.method == 'POST':
        # Check if user enters correct credentials
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']  # Add email field
        
        # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another username.")
            return render(request, 'signup.html')
        
        # Create a new user if the username is not taken
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Your account has been successfully created. Login to continue.")
        
    return render(request, 'signup.html')