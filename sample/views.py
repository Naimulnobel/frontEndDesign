from . import views
from django.shortcuts import render,redirect

def home(request):
    
    return render(request, 'index.html')

