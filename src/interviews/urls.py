from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_interviews, name='list_interviews'),
]
