from django.shortcuts import render
from rest_framework.response import Response
from . models import Company,Employee
from . serializers import CSerializer, CompSerializer, CompanySerializer, ESerializer,EmployeeSerializer
from rest_framework.views import APIView
# Create your views here.
class ListAll(APIView):
    def get(self,request):
        type = request.GET.get('type',None)
        if type == "comp":
            company = Company.objects.all()
            serializer = CSerializer(company, many=True)
        elif type == "emp":
            employee = Employee.objects.all()
            serializer = ESerializer(employee,many=True)
        else:
            return Response({'msg':'Invalid'})
        return Response(serializer.data)

class Companywisedetail(APIView):
    def get(self,request):
        type = request.GET.get('type',None)
        if type =="dell":
            company = Employee.objects.all()
            serializer = EmployeeSerializer(company, many=True)
        elif type == "acer":
            company = Employee.objects.all()
            serializer = EmployeeSerializer(company, many=True)
        else:
            return Response({'msg':'no employee found'})
        return Response(serializer.data)


class Employeedetail(APIView):
    def get(self,request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

class Createcompany(APIView):
    def post(self,request):
        serializer = CompSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CreateEmployee(APIView):
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class Employeedetail_all(APIView):
    def get(self,request, format=None):
        name_of_company=request.GET.get('name_of_company',None)
        comp_obj = Company.objects.filter(Company_name__iexact=name_of_company).last()
        comp_id=comp_obj.id
        company = Employee.objects.filter(Company=comp_id)
        serializer = EmployeeSerializer(company, many=True)
        return Response(serializer.data)
