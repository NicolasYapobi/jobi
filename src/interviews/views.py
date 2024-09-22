from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Interview
from .forms import InterviewForm, RegisterForm



########################
# Register functions   #
########################
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

########################
# Login functions      #
########################



########################
# Interviews functions #
########################
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

