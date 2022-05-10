from django.shortcuts import render
from rest_framework.response import Response
from . models import Staff
from . serializers import StaffSerializer
from rest_framework.views import APIView
# Create your views here.
class ListStaff(APIView):
    def get(self,request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

class Staffdetail(APIView):
    def get(self,request,pk, format=None):
        staff = Staff.objects.filter(id=pk).last()
        serializer = StaffSerializer(staff, many=False)
        return Response(serializer.data)

class Createstaff(APIView):
    def post(self,request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateStaff(APIView):
    def put(self,request,pk):
        staff = Staff.objects.get(id=pk)
        serializer = StaffSerializer(staff,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteStaff(APIView):
    def delete(self,request,pk):
        #staff = Staff.objects.get(id=pk)
        staff_instance = Staff.objects.get(id=pk)
        staff_instance.delete()
        return Response('Deleted')