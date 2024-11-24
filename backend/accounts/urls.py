from django.urls import path
from .views import RecordsOfficerRegisterView, RecordsManagerRegisterView

urlpatterns = [
    path('accounts/register/officer', RecordsOfficerRegisterView.as_view(), name='officer_register'),

    path('accounts/register/manager', RecordsManagerRegisterView.as_view(), name='manager_register'),


]
