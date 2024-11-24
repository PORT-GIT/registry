from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

class RecordsSystemUser(AbstractUser):
    is_records_officer = models.BooleanField(default=False)
    is_records_manager = models.BooleanField(default=False)

class RecordsManager(models.Model):
    user = models.OneToOneField(RecordsSystemUser, primary_key=True, on_delete=models.CASCADE)
    manager_id = models.CharField(max_length=11, unique=True, blank=False)
    organization = models.CharField(max_length=70, blank=False)


class RecordsOfficer(models.Model):
    user = models.OneToOneField(RecordsSystemUser, primary_key=True, on_delete=models.CASCADE)
    officer_id = models.CharField(max_length=11, unique=True, blank=False)
    supervisor = models.ForeignKey(RecordsManager, on_delete=models.SET_NULL, null=True)
    
