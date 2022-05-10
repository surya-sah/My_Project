from django.urls import path
from . views import *

urlpatterns = [
    path('',List.as_view(),name='All'),
    path('createproduct/',Createproduct.as_view(),name='Product_create'),
    path('createsales/',CreateSalesDate.as_view(),name='Sales_create'),
    path('test/',Test.as_view(),name='test'),
    path('add_up_product/',addproduct.as_view(),name='addproduct')

]
