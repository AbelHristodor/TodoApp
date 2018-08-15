from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import get_object_or_404

from .models import Todo
from .forms import TodoForm
import json

success_response = {"success": True}

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()             
        return HttpResponse(json.dumps(success_response), content_type="application/json")

def delete_todo(request):
    if request.method == "POST":
        task = Todo.objects.get(pk=request.POST['id'])
        task.delete()
        return HttpResponse(json.dumps(success_response), content_type="application/json")

def delete_all(request):
    if request.is_ajax():
        tasks = Todo.objects.all()
        tasks.delete()
        return HttpResponse(json.dumps(success_response), content_type="application/json")

def get_todos(request):
    if request.is_ajax():
        todos = Todo.objects.all().order_by('created_date').reverse()
        data = serializers.serialize("json", todos)
        return HttpResponse(data, content_type="application/json")


def update_todo(request):
    if request.method == "POST":
        task = get_object_or_404(Todo, pk=request.POST['id'])
        form = TodoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(success_response), content_type="application/json")

        
