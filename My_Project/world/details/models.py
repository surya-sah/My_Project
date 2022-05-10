
from django.db import models

# Create your models here.
class country(models.Model):
    sortname = models.CharField(max_length=50, blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    phoneCode = models.CharField(max_length=50, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField(null=True, blank=True)
class state(models.Model):
    name = models.CharField(max_length=50, blank=True,null=True)
    country_id = models.ForeignKey(country, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField(null=True, blank=True)
class city(models.Model):
    name = models.CharField(max_length=50, blank=True,null=True)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField(null=True, blank=True)