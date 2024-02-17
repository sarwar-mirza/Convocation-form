from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class Student(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    
    name_of_degree = models.CharField(max_length=50)
    admission_session = models.IntegerField()
    reg_no = models.IntegerField()
    batch = models.IntegerField()
    graduating_session = models.IntegerField()
    cgpa = models.FloatField()
