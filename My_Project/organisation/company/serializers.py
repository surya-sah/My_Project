from django.db.models import fields
from rest_framework import serializers
from .models import Company, Employee

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class ESerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','Employee_name','Company',]


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    company_name = EmployeeSerializer(many=True,read_only=True)
    class Meta:
        model = Company
        fields = ['Company_name','Website','Address','Email','company_name']

