from django.urls import path
from .views import *

urlpatterns = [
    # path('',CountryAPI.as_view(),name='All'),
    path('country/',CountryAPI.as_view(),name='All'),
    path('state/',StateAPI.as_view(),name='All'),
    path('city/',CityAPI.as_view(),name='All'),
    path('country_list/',searchdataList.as_view(),name='All'),
    path('country_list_page/',CountryListView.as_view(),name='3333'),


]