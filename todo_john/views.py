from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
# Create your views here.

def todo(request):
    if request.method == 'POST':
        todo_title = request.POST.get('todo_title') 
        todo_desc = request.POST.get('todo_desc') 
        todo_pos = Todo(title = todo_title, desc = todo_desc)
        todo_pos.save()
       
        messages.success(request, "Todo Added Successfully")
        return redirect('todo')
    todop = Todo.objects.all()
    return render (request, 'todo.html', {'todo_pos':todop})

def delete_todo(request, id):
    todo_to_delete=Todo.objects.get(id=id)
    todo_to_delete.delete()
    messages.success(request, "Todo Deleted Successfully")
    return redirect('todo')
