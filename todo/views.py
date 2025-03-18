from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def signup(requests):
    return render(requests,'signup.html')

def loginn(requests):
    return render(requests,'login.html')