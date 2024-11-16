from django.contrib import admin
from .models import RecordsUserAccount, RecordsOfficer, RecordsManager

# Register your models here.
admin.site.register(RecordsUserAccount)
admin.site.register(RecordsOfficer)
admin.site.register(RecordsManager)
