from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def signup(requests):
    return HttpResponse("Signup button")