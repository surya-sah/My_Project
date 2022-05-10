from django.db import models

# Create your models here.
class Company(models.Model):
    Company_name = models.CharField(max_length=70, blank=True,null=True)
    Website = models.CharField(max_length=200,blank=True,null=True)
    Address = models.CharField(max_length=70, blank=True,null=True)
    Email = models.EmailField(max_length=254)
class Employee(models.Model):
    Employee_name = models.CharField(max_length=70, blank=True,null=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='company_name')
    Address = models.CharField(max_length=70, blank=True,null=True)
    Phone_number = models.CharField(max_length=12)
    City = models.CharField(max_length=200,blank=True,null=True)
    State = models.CharField(max_length=200,blank=True,null=True)

