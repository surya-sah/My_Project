
from rest_framework import serializers
from .models import *





class StatenewSerializers(serializers.ModelSerializer):
    class Meta:
        model = state
        fields =  "__all__"

class CitySerializers1(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()
    class Meta:
        model = city
        fields = ['id','name','state_id','is_active','effective_from','state_name']
    def get_state_name (self,obj):
        print(obj.state_id.id,"=============")
        sst = state.objects.filter(id = obj.state_id.id).values("id")
        dd = StatenewSerializers(sst, many = True)
    
class CountrySerializers(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    class Meta:
        model = country
        fields = ['id','name','sortname','phoneCode','state_name','city_name']
    def get_state_name (self,obj):
        print (obj.id)
        st_name=state.objects.filter(country_id= obj.id).values("name")
        return st_name
    def get_city_name (self,obj):
        print (obj.id)
        st_name=state.objects.filter(country_id= obj.id).values("id")
        city_name=city.objects.filter(state_id__in=st_name).values("name")
        return city_name


class StateSerializers(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()
    country_sn = serializers.SerializerMethodField()
    country_state = serializers.SerializerMethodField()
    class Meta:
        model = state
        fields = ['name','country_id','is_active','effective_from','country_name','country_sn','country_state']
    def get_country_name (self,obj):
        return (obj.country_id.name)
    def get_country_sn (self,obj):
        return (obj.country_id.sortname)
    def get_country_state (self,obj):
        return (obj.country_id.name) + "," + (obj.name)

class CitySerializers(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()


    class Meta:
        model = city
        fields = ['name','state_id','is_active','effective_from','state_name','country_name']
    def get_state_name (self,obj):
        return (obj.state_id.name)
    def get_country_name (self,obj):
        return (obj.state_id.country_id.name)

class SearchSerializers(serializers.ModelSerializer):
    state_name = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    csc_join = serializers.SerializerMethodField()


    class Meta:
        model = city
        fields = ['name','state_name','country_name','csc_join']
    def get_state_name (self,obj):
        return (obj.state_id.name)
    def get_country_name (self,obj):
        return (obj.state_id.country_id.name)
    def get_csc_join (self,obj):
        return (obj.name)+","+(obj.state_id.name)+","+(obj.state_id.country_id.name)



class CountrySerializerss(serializers.ModelSerializer):
   
    class Meta:
        model = country
        fields = ['id','name','sortname','phoneCode']