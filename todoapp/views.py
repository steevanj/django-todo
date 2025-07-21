from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from todoapp.models import todomodel
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')  

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('todoapp')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def todoapp(request):
    if request.method == 'POST':
        task = request.POST.get('title')
        todomodel.objects.create(title=task, user=request.user)
        tasks = todomodel.objects.filter(user = request.user)
        return render(request, 'todo.html', {'tasks': tasks})
    tasks = todomodel.objects.filter(user = request.user)
    return render(request, 'todo.html', {'tasks':tasks})

@login_required(login_url='login')
def edit_todo(request, srno):
    task = get_object_or_404(todomodel, srno=srno, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('todoapp')
    return render(request, 'edit_todo.html', {'task': task})

@login_required(login_url='login')
def delete_todo(request, srno):
    task = get_object_or_404(todomodel, srno=srno, user=request.user)
    task.delete()
    return redirect('todoapp')

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')