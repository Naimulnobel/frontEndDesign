import datetime
from datetime import datetime

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect, redirect,
                              render)
from django.views.decorators.csrf import *

from .models import *

# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect("login")


def login(request):
    return render(request, "login.html")


def loginCheck(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                user.save()
                if request.user.is_superuser is True :
                    print("logged in successfully")
                    message = "you are successfully logged in"
                    messages.success(request, message)
                    return redirect("dashBoard")
                else:
                    auth.logout(request)
                    return redirect('home')
            else:
                print("wrong username and password")
                return redirect("login")
        else:
            print("login failed")
            return redirect("login")
    else:
        print("login problem")
        return redirect("login")

def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url="loginPage")
def dashBoard(request):
    
    return render(request, 'index.html')

def customerLogin(request):
    return render(request, "customerLogin.html")



def customerloginCheck(request):
    print('gotit')
    if request.method == "POST":
        print("yo")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print('username :', username)
        if username and password :
           user = authenticate(username=username, password=password)
           if user is not None:
                auth_login(request, user)
                user.save()
                print("logged in successfully")
                message = "you are successfully logged in"
                messages.success(request, message)
                return redirect("home")
           else:
                print("wrong username and password")
                return redirect("customerLogin")
        else :
            print("login failed")
            return redirect("customerLogin")
    else:
        print("login problem")
        return redirect("customerLogin")

def customerRegistration(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        passwordOne = request.POST.get("password")
        lastLogin = datetime.now()
        dateJoined = datetime.now()
        User.objects.create_user(
            username=firstName + lastName,
            first_name=firstName,
            last_name=lastName,
            email=email,
            is_superuser=0,
            is_staff=0,
            password=passwordOne,
            last_login=lastLogin,
            date_joined=dateJoined,
            is_active=1,
        )
        message = 'User Registration Successful'
        messages.success(request, message)
        return render(request, 'customerLogin.html')
    else:
        print("else block")
        return render(request, "customerLogin.html")


def customerLogout(request):
    auth.logout(request)
    return redirect("home")
def profile(request):
    return render(request, 'profile.html')
