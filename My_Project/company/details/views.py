from django.shortcuts import render
from rest_framework.response import Response
from . models import Employee,Company
from . serializers import EmployeeSerializer,CompanySerializer
from rest_framework.views import APIView


# Create your views here.
class ListCompanyAPIView(APIView):
    def get(self,request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

class ComapnydetailAPIView(APIView):
    def get(self,request,pk):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

class CreateCompanyAPIView(APIView):
    def post(self,request):
        #print(request.data)
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateCompanyAPIView(APIView):
    def post(self,request,pk):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteCompanyAPIView(APIView):
    def get(self,request,pk):
        company = Company.objects.get(id=pk)
        company_instance = Company.objects.get(id=pk)
        company_instance.delete()
        return Response('Deleted')


class ListEmployeeAPIView(APIView):
    def get(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

class EmployeedetailAPIView(APIView):
    def get(self,request,pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee, many=False)
        return Response(serializer.data)

class CreateEmployeeAPIView(APIView):
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateEmployeeAPIView(APIView):
    def post(self,request,pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteEmployeeAPIView(APIView):
    def get(self,request,pk):
        employee = Employee.objects.get(id=pk)
        employee_instance = Employee.objects.get(id=pk)
        employee_instance.delete()
        return Response('Deleted')

