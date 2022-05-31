import imp
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/contacts/")
    return render(request, "users/login.html", {"form":form})
