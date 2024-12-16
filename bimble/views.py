from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Child

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('children_list')
    return render(request, 'login.html')

def blog(request):
    return render(request, 'blog.html')

def jam_kerja(request):
    return render(request, 'jam_kerja.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def children_list(request):
    children = Child.objects.all()
    return render(request, 'children_list.html', {'children': children})