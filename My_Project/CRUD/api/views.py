from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employees, Item
from api.serlializers import ItemSerializer
from api.serlializers import employeeSerializer

@api_view(['GET'])
def ApiOverview(request):
	return Response({'message':'hello surya'})


@api_view(['POST'])
def add_items(request):
	item = ItemSerializer(data=request.data)

	# validating for already existing data
	if Item.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_employee(request):
	employee = employeeSerializer(data=request.data)

	# validating for already existing data
	if Employees.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if employee.is_valid():
		employee.save()
		return Response(employee.data)
	else:
		print(employee.errors)
		return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

