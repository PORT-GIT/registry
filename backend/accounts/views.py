from django.shortcuts import render
from .serializers import OfficerRegistrationSerializer, ManagerRegistrationSerializer
from .models import RecordsOfficer, RecordsManager
from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

#assuming that there is an employee database with assigned roles to the employees once the
class RecordsOfficerRegisterView(CreateAPIView):
    #this view registers the system users
    pass
    

class RecordsManagerRegisterView(CreateAPIView):
    #this view registers the system users
    pass

class RecordsOfficerListView(ListAPIView):
    #this view lists all records officer
    pass
    #this defines the queryset
    #queryset = RecordsOfficer.objects.all()
    #serializer_class = RecordsOfficerSerializer

class RecordsManagerListView(ListAPIView):
    #this view lists all records manager
    pass
    #this defines the queryset
    #queryset = RecordsManager.objects.all()
    #serializer_class = RecordsManagerSerializer




# Create your views here.
