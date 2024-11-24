from django.urls import path
from .views import RecordsOfficerRegisterView, RecordsManagerRegisterView

urlpatterns = [
    path('register_officer/', RecordsOfficerRegisterView.as_view(), name='register_officer'),

    path('register_manager/', RecordsManagerRegisterView.as_view(), name='register_manager'),


]
