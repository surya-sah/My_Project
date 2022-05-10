from unicodedata import name
from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from django.db.models import Q
from rest_framework import generics
from . serializers import *
from rest_framework.views import APIView
from rest_framework import filters
from django.views.generic.list import ListView
from django.views.generic import ListView
from details.models import country

from details.pagination import GpiPagination


# Create your views here.
class CountryAPI(APIView):
    def post(self,request):
        for i in request.data["countries"]:
            serializer = CountrySerializers(data = i)
            if serializer.is_valid():
                serializer.save()
        return Response({'msg':"success"})
    def get(self, request):
        a = request.GET.get("id",None)
        print(a)
        if a is not None:
            country1=country.objects.filter(Q(id=a)|Q(name = a))
            serializer = CountrySerializers(country1, many=True)
        else:
            country1 = country.objects.all()
            serializer = CountrySerializers(country1, many=True)
        return Response(serializer.data)



class StateAPI(APIView):
    def post(self,request):
        for i in request.data["states"]:
            serializer = StateSerializers(data = i)
            if serializer.is_valid():
                serializer.save()
        return Response({'msg':"success"})
    def get(self, request):
        a = request.GET.get("country_id",None)
        print(a)
        if a is not None:
            state1=state.objects.filter(country_id=a)
            serializer = StateSerializers(state1, many=True)
        else:
            state1 = state.objects.all()
            serializer = StateSerializers(state1, many=True)
        return Response(serializer.data)



class CityAPI(APIView):
    def post(self,request):
        for i in request.data["cities"]:
            serializer = CitySerializers(data = i)
            if serializer.is_valid():
                serializer.save()
        return Response({'msg':"success"})
    def get(self, request):
        a = request.GET.get("state_id",None)
        print(a)
        if a :
            print("777777")
            city1=city.objects.filter(state_id=a)
            print(city1,'======')
            serializer = CitySerializers(city1, many=True)
        else:
            print("pppppp")
            city1 = city.objects.all()
            serializer = CitySerializers(city1, many=True)
        return Response(serializer.data)

class searchList(generics.ListAPIView):
        queryset =country.objects.all()
        serializer_class = CountrySerializers
        filter_backends = (filters.SearchFilter,)
        search_fields = ['=name','id']


class searchdataList(generics.ListAPIView):
        queryset =city.objects.all()
        serializer_class = SearchSerializers
        filter_backends = (filters.SearchFilter,)
        search_fields = ['name','state_id__name','state_id__country_id__name']
      
class CountryListView(generics.ListAPIView):
    # model = country
    serializer_class = CountrySerializerss
    pagination_class = GpiPagination
    def get_queryset(self):
        # queryset = country.objects.all()
        return country.objects.all()