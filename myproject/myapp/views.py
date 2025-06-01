from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        UserModel.objects.create(
            username = username,
            email = email,
            password = password
        ).save()
        return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if UserModel.objects.filter(email=email, password=password).exists():
            return redirect('about')
        else:
            return redirect('signup')
        
    return render(request, 'signin.html')

def about(request):
    return render(request, 'about.html')

def todo(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('todo')
    return render(request, 'todo.html', {'tasks':tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed =  not task.completed
    task.save()
    return redirect('todo')