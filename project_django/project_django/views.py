from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5 + 10
    return render(request, 'about.html', {'h': a})

def home(request):
    return HttpResponse('This is my home')