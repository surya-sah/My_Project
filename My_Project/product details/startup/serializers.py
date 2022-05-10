from django.db.models import fields
from rest_framework import serializers
from .models import Product, SalesDate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class SalesDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDate
        fields = '__all__'
class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDate
        fields = '__all__'
        