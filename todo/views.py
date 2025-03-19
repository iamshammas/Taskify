from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def signup(requests):
    if requests.method == 'POST':
        unm = requests.POST.get('unm')
        email = requests.POST.get('email')
        pwd = requests.POST.get('pwd')
        userr = User.objects.create_user(username=unm,email=email,password=pwd)
        userr.save()
        return redirect('loginn')
    else:
        pass
    return render(requests,'signup.html')

def loginn(requests):
    if requests.method == 'POST':
        unm = requests.POST.get('unm')
        pwd = requests.POST.get('pwd')
        myuser = authenticate(username=unm,password=pwd)
        myuser.save()
        return redirect('dashboard')
    return render(requests,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def add_task(request):
    return HttpResponse("add_task")

def logout_user(request):
    logout(request)
    return redirect('loginn')