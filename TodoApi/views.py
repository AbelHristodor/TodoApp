from django.shortcuts import render
from api.models import Todo

def home(request):
    return render(request, "home.html")