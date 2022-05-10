from itertools import product
from unicodedata import category
from urllib import response
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from . models import Product,SalesDate
from . serializers import ProductSerializer, SalesDateSerializer,PSerializer,SaleSerializer
from rest_framework.views import APIView
import datetime

# Create your views here.
class List(APIView):
    def get(self,request):
        type = request.GET.get('type',None)
        if type == "product":
            product = Product.objects.all()
            serializer = PSerializer(product, many=True)
        elif type == "salesdata":
            salesdata = SalesDate.objects.all()
            serializer = SaleSerializer(salesdata,many=True)
        else:
            return Response({'msg':'Invalid'})
        return Response(serializer.data)
class Createproduct(APIView):
    def post(self,request):
        print("hii")
        print(request.data)

        for i in request.data:
            # print(request.data)
            print(i)

            serializer = ProductSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
        return Response({"msg":"success"})
        # return Response(serializer.errors)

class CreateSalesDate(APIView):
    def post(self,request):
        serializer = SalesDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Test(APIView):
    def get(self, request):
        # product = Product.objects.all().values_list("Category","Product_name")
        # print (product)
        records = Product.objects.all()
        records.delete()

        return None
class addproduct(APIView):
    def post(self,request):
        data = request.data
        for i in data :
            i["create_date"] = datetime.datetime.now()
            i["update_date"] = datetime.datetime.now()
            i["Category"]=i["category_name"]
            i["Product_name"] = i["product_name"]
            datavar =Product.objects.filter(Product_name = i['product_name'] ,Product_code = i['Product_code']).last()
            if datavar:
                i.pop("create_date")
                serialiser =ProductSerializer(datavar,data = i)
                if serialiser.is_valid():
                    serialiser.save()
            else:
                i.pop("update_date")
                serialiser =ProductSerializer(data = i)
                if serialiser.is_valid():
                    serialiser.save()
        return Response({"Message":"success"})


