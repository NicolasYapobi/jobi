from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Interview
from .forms import InterviewForm

def list_interviews(request):
    interviews = Interview.objects.all()
    return render(request, 'interviews/list.html', {'interviews': interviews})

def add_interview(request):
    if request == "POST":
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_interviews')
    else:
        form = InterviewForm()
    return render(request, 'interviews/add_interview.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_interviews')
        else:
            return render(request, 'interviews/login.html', {'error': 'Invalid credentials'})
    return render(request, 'interviews/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

