from django.shortcuts import render
from .models import Interview

def list_interviews(request):
    interviews = Interview.objects.all()
    return render(request, 'interviews/list.html', {'interviews': interviews})