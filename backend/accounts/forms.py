from django.forms import forms
from .models import RecordsOfficer, RecordsManager

class RecordsOfficerRegistrationForm(forms.ModelForm):
    
    class Meta:
        #model = RecordsOfficer
        pass

class RecordsManagerRegistrationForm(forms.ModelForm):
    
    class Meta:
        #model = RecordsManager
        pass