from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import emp
from datetime import datetime
from django.urls import reverse
from .forms import *

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Invalid username or password"))
            return redirect('loginuser')

    else:
        return render(request, 'myapp/login.html')
def home(request):
    return render(request, 'myapp/Home.html')
def add_emp(request):
    
    form = EmployeeForm()
    if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                employee = form.save()
                return redirect('home')   
    context = {
            'form': form,
        }

    return render(request, 'myapp/ADd.html',context)
def view_emp(request):
    employees = emp.objects.all()
    return render(request, 'myapp/viewemp.html', {'employees': employees})

def grievances(request):
    return HttpResponse('grievances')
def manager_info(request):
    return render(request, 'myapp/Managers.html')
def department(request):
    return render(request, 'myapp/departm.html')
