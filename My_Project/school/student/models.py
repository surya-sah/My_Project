from django.db import models

# Create your models here.
class Student(models.Model):
    First_name = models.CharField(max_length=70, blank=True,null=True)
    Last_name = models.CharField(max_length=200,blank=True,null=True)
    Address = models.CharField(max_length=70, blank=True,null=True)