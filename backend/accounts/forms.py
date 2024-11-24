from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  RecordsOfficer, RecordsManager


#i have used the recordssystemuser as the model in the forms because i have used
#that model to inherit the basic USER model from django

#i have similarly done the same by inheriting and extending the RECORDSSYTEMUSER model
#to the two users of the system.
#CURRENTLY OMMITTED THE NEED FOR THE RECORDSSYSTEMUSER MODEL BUT WILL KEEP COMMENT

#for the registration forms the added fields will bw written above the class Meta

class OfficerRegistrationForm(UserCreationForm):
    officer_id = forms.CharField(max_length=20)
    
    class Meta:
        model = RecordsOfficer
        fields = ['username', 'email', 'officer_id']

class ManagerRegistrationForm(UserCreationForm):
    manager_id = forms.CharField(max_length=20)

    class Meta:
        model = RecordsManager
        fields = ['username', 'email', 'manager_id']