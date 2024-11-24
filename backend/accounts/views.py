from django.shortcuts import render
# from .serializers import RecordsUserSerializer, RecordsOfficerSerializer, RecordsManagerSerializer
from .models import RecordsOfficer, RecordsManager
from django.http import Http404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from rest_framework.response import Response
from rest_framework import status

#assuming that there is an employee database with assigned roles to the employees once the
class RecordsOfficerRegisterView(CreateView):
    #this view registers the system users
    pass

class RecordsOfficerRegisterView(CreateView):
    #this view registers the system users
    pass    

class RecordsManagerRegisterView(CreateView):
    #this view registers the system users
    pass

class RecordsOfficerListView(ListView):
    #this view lists all records officer
    pass
    #this defines the queryset
    #queryset = RecordsOfficer.objects.all()
    #serializer_class = RecordsOfficerSerializer

class RecordsManagerListView(ListView):
    #this view lists all records manager
    pass
    #this defines the queryset
    #queryset = RecordsManager.objects.all()
    #serializer_class = RecordsManagerSerializer




# Create your views here.
