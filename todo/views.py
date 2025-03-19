from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from todo.models import Task
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
        if myuser is not None:
            login(requests,myuser)
        else:
            pass
        return redirect('dashboard')
    return render(requests,'login.html')

def dashboard(request):
    items = Task.objects.filter(user=request.user)
    context = {
        'items' : items
    }
    return render(request,'dashboard.html',context)

def add_task(request):
    if request.method == 'POST':
        get_title = request.POST.get('title')
        new_task = Task.objects.create(title=get_title,user = request.user)
        new_task.save()
    return redirect('dashboard')

def update_task(request):
    return HttpResponse("Update Task")

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('dashboard')

def logout_user(request):
    logout(request)
    return redirect('loginn')