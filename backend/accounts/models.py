from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#using managers is optional but it improves the organization and the querying of users
#based on their roles
#it will not however assist in separating user registration by roles
#can be called on in the views that will query the database for the users
# class RecordsSystemUserManager(BaseUserManager):
#     def managers(self):
#         return self.filter(role='RecrordsManager')
    
#     def officers(self):
#         return self.filter(role='RecrordsOfficer')


# class RecordsSystemUser(AbstractUser):
#     is_records_officer = models.BooleanField(default=False)
#     is_records_manager = models.BooleanField(default=False)

##decided to try a simpler method of creating users models

class RecordsManager(User):
    # user = models.ForeignKey(User, related_name='managers', primary_key=True, on_delete=models.CASCADE)
    manager_id = models.CharField(max_length=20, blank=False)
    

class RecordsOfficer(User):
    # user = models.ForeignKey(User, related_name='officers', primary_key=True, on_delete=models.CASCADE)
    officer_id = models.CharField(max_length=20, blank=False)
    
