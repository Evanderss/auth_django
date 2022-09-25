from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
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

def singout(request):
    logout(request)
    return redirect("home")