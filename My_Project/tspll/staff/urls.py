from django.urls import path
from . views import *

urlpatterns = [
    path('',ListStaff.as_view(),name='staff'),
    path('detail/<int:pk>/',Staffdetail.as_view(),name='staff_detail'),
    path('create/',Createstaff.as_view(),name='staff_create'),
    path('update/<str:pk>/',UpdateStaff.as_view(),name='staff_update'),
    path('delete/<str:pk>/',DeleteStaff.as_view(),name='staff_delete'),
]