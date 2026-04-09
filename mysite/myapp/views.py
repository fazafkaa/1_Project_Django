# from django.shortcuts import render

# def home(request):
#     return render(request, 'myapp/index.html')
    
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def skills(request):
    return render(request, 'myapp/skills.html')

def projects(request):
    return render(request, 'myapp/projects.html')

def contact(request):
    return render(request, 'myapp/contact.html')