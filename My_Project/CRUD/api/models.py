from django.db import models

# Create your models here.

#Employee
class Employees(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Dept_name = models.CharField(max_length=20)
    joining_date = models.DateField()
    salary = models.IntegerField()
# Items


class Item(models.Model):
	category = models.CharField(max_length=255,null=True)
	employees = models.ForeignKey(Employees,on_delete=models.CASCADE,null=True)
	subcategory = models.CharField(max_length=255,null=True)
	name = models.CharField(max_length=255,null=True)
	amount = models.PositiveIntegerField(default=0)




