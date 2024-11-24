from rest_framework import serializers
from .models import RecordsOfficer, RecordsManager

class OfficerRegistrationSerializer(serializers.ModelSerializer):
    officer_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = RecordsOfficer
        fields = '__all__'
    

class ManagerRegistrationSerializer(serializers.ModelSerializer):
    manager_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = RecordsManager
        fields = '__all__'