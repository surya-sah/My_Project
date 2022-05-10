from django.db.models import fields
from rest_framework import serializers
from .models import Employees, Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		#fields = ('category', 'subcategory', 'name', 'amount')
		fields = '__all__'
class employeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employees
		#fields = ('category', 'subcategory', 'name', 'amount')
		fields = '__all__'