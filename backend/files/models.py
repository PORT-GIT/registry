from django.db import models

# Create your models here.
class Classification(models.Model):
    classification = models.CharField(max_length=100)


class File(models.Model):
    ORGANIZATION_DEPARTMENT = (
        ('HUMANRESOURCES', 'HRM'),
        ('FINANCE', 'FIN'),
        ('ICT', 'ICT'),
        ('PUBLICCOMMUNICATION', 'PUB'),
        ('PROPERTYMANAGEMENT', 'PRM'),
        ('ADMINISTARTION', 'ADM'),
        ('REPORTS', 'REP'),
        ('CONFIDENTIAL', 'CNF'),
        ('CLAIMS&BENEFITS', 'CBN'),
        ('TRANSPORT', 'TRS'),
        ('MEMBERSHIP', 'MEM'),
        ('PROCUREMENT', 'PRC'),
        ('HOSPITALS', 'HSP'),
        ('LEGAL', 'LEG'),
        ('STANDARDS', 'STD'),
    )
    file_name = models.CharField(max_length=100, blank=False)
    file_department = models.CharField(max_length=100, choices=ORGANIZATION_DEPARTMENT)
    file_classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    date_opened = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.file_name+"   "+ self.file_classification


class FileMovement(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    date_moved = models.DateField(auto_now_add=True)
    receiving_department = models.CharField(max_length=100)


class FileClosed(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    date_closed = models.DateField(auto_now_add=True)
        