from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth import logout
def home(request):
    return render(request,'home.html')

@login_required
def todo(request):
    tasks = Todo.objects.filter(user=request.user).annotate(
        priority_val=Case(
            When(priority='high', then=Value(1)),
            When(priority='medium', then=Value(2)),
            When(priority='low', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('priority_val', '-created_at')
    return render(request, 'dashboard.html', {'tasks': tasks})
    
def logout_view(request):
    logout(request)
    return redirect('myapp:home')

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        priority=request.POST.get('priority', 'medium')
        Todo.objects.create(
            user=request.user,
            title=title,
            priority=priority,
        )
        return redirect('myapp:todo')
    
def delete_task(request,id):
    task=get_object_or_404(Todo,id=id,user=request.user)
    task.delete()
    return redirect('myapp:todo')

def update_task(request,id):
    task=get_object_or_404(Todo,id=id,user=request.user)
    if request.method=="POST":
        new_title=request.POST.get('title')
        task.priority = request.POST.get('priority', 'medium')
        task.title=new_title
        task.save()
        return redirect('myapp:todo')
    return render(request,'edit.html',{'task':task})

def update_status(request,id):
    task=get_object_or_404(Todo,id=id,user=request.user)
    if task.completed==True:
        task.completed=False
        task.save()
    else:
        task.completed=True
        task.save()
    return redirect('myapp:todo')

def demo_view(request):
    return render(request, 'demo.html')