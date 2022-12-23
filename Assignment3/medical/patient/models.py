from django.db import models
from django.utils import timezone

# Create your models here

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    patient_registration_number = models.IntegerField()
    patient_name = models.CharField(blank=True,null=True,max_length=122)
    patient_email = models.EmailField(blank=True,null=True,max_length=122)
    patient_mobile_number = models.IntegerField()
    admitted_at = models.TimeField(default=timezone.now)


    def __str__(self):
        return self.patient_name