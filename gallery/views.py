from django import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def staff_registration_form(request):
    return render(request,'staff_registration_form.html')

def customer_registration_form(request):
    return render(request,'customer_registration_form.html')