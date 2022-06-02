import imp
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login
from .forms import LoginForm, SignupForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/contacts/")
        else:
            msg = "Nom d'utilisateur ou mot de passe non valide"
            form = LoginForm(request.POST)
            return render(request, "users/login.html", {"form":form, "msg":msg})
    return render(request, "users/login.html", {"form":form})

def register_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
    else:
        form = SignupForm()
    return render(request, "users/register.html", {"form":form})