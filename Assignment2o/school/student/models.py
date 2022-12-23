from django.db import models

# Create your models here.

class Student_list(models.Model):
    id = models.AutoField(primary_key=True)
    student_regNo = models.IntegerField()
    student_name = models.CharField(max_length=50,null=True,blank=True)
    student_email = models.CharField(max_length=50,null=True,blank=True)
    student_mobile = models.IntegerField()
    created_at = models.DateField()
    

    def __str__(self):
        return self.student_name