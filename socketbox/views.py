from django.shortcuts import render

def index(request):
    return render(request, 'socketbox/index.html', {})

def profile(request):
    return index(request)