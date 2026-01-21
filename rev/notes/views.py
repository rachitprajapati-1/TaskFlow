from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes_list.html', {'notes': notes})

@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        color = request.POST.get('color')
        
        Note.objects.create(user=request.user, title=title, content=content, color=color)
        return redirect('notes:list') 
    
    return render(request, 'add_note.html')

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    return redirect('notes:list')

@login_required
def edit_note(request,id):
    note=get_object_or_404(Note,id=id,user=request.user)
    if request.method=='POST':
        new_title=request.POST.get('title')
        new_content=request.POST.get('content')
        new_color=request.POST.get('color')
        note.title=new_title
        note.content=new_content
        note.color=new_color
        note.save()
        return redirect('notes:list')
    return render(request,'edit_note.html',{'note':note})