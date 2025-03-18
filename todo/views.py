from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
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
    return render(requests,'login.html')