from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
  form = UserCreationForm(request.POST or None)

  if form.is_valid():
    form.save()

    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password1")

    user = authenticate(username=username, password=password)

    login(request, user)
    return redirect("home")

  return render(request, "accounts/signup.html", {"form": form})
