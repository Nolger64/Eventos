from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

