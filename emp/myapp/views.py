from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def loginUser(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print(user)
        return redirect('home')

    return render(request, 'myapp/login.html')
def home(request):
    return HttpResponse('home')
def add_emp(request):
    return render(request, 'myapp/ADd.html')