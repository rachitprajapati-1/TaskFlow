from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib.auth import logout
def home(request):
    return render(request,'home.html')

@login_required
def todo(request):
    tasks = Todo.objects.filter(user=request.user) # Filter by current user
    return render(request, 'dashboard.html', {'tasks': tasks})
    
def logout_view(request):
    logout(request)
    return redirect('myapp:home')

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Todo.objects.create(
            user=request.user,
            title=title
        )
        return redirect('myapp:todo')