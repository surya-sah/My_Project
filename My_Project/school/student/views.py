from django.shortcuts import render
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer
from rest_framework.views import APIView
# Create your views here.
class ListStudentAPIView(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

class StudentdetailAPIView(APIView):
    def get(self,request,pk, format=None):
        student = Student.objects.filter(id=pk).last()
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)

class CreatestudentAPIView(APIView):
    def post(self,request):
        #print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateStudentAPIView(APIView):
    def post(self,request,pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteStudentAPIView(APIView):
    def get(self,request,pk):
        student = Student.objects.get(id=pk)
        student_instance = Student.objects.get(id=pk)
        student_instance.delete()
        return Response('Deleted')