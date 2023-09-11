from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'hello/index.html')

def greet(request, name):
    name = request.GET.get(name)
    return render(request, 'hello/greet.html', name)