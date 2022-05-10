
from django.db import models

# Create your models here.
class Product(models.Model):
    Category = models.CharField(max_length=50, blank=True,null=True)
    Product_name = models.CharField(max_length=50,blank=True,null=True)
    Product_code = models.CharField(max_length=50, blank=True,null=True)
    Price = models.FloatField(blank=True,null=True)
    status = models.BooleanField(default=True)
    date_time = models.DateTimeField(blank=True,null=True)
    create_date = models.DateTimeField(blank=True,null=True)
    update_date = models.DateTimeField(blank=True,null=True)
class SalesDate(models.Model):
    User = models.CharField(max_length=50, blank=True,null=True)
    Product_code = models.CharField(max_length=50, blank=True,null=True)
    Product_name = models.CharField(max_length=50, blank=True,null=True)
    Town_sale = models.FloatField(blank=True,null=True)
    Local_sale = models.FloatField(blank=True,null=True)
    Price = models.FloatField(blank=True,null=True)
    Date = models.DateField(null = True)
