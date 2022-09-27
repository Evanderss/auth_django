from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
# Create your views here.
def home(request):
    return render(request, "home.html")

def singup(request):
    if request.method == "GET":
        print("enviando formulario")
        return render(request, "signup.html", {
            "form" : UserCreationForm 
    } )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            #register user
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError: 
                return render(request, "signup.html", {
                    "form" : UserCreationForm ,
                    "error" : "El usuario ya existe"
                })
        return render(request, "signup.html", {
            "form" : UserCreationForm ,
            "error" : "Las contraseñas no coinciden"
    })


def tasks(request):
    return render(request, "tasks.html") 

def create_tas(request):
    if request.method == "GET":
        return render(request, "create_tas.html", {
        "form": TaskForm
        })
    else: 
        print(request.POST)
        return render(request, "create_tas.html", {
        "form": TaskForm
        })

def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
        "form": AuthenticationForm
    })
    else: 
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {
            "form": AuthenticationForm,
            "error": "Username or password is incorrect"})
        else:
            login(request, user)
            return redirect("tasks")