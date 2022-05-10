#./todo/views.py

from django.urls import path
from . views import *

urlpatterns = [
    path('',ListCompanyAPIView.as_view(),name='company'),
    path('companydetail/<str:pk>/',ComapnydetailAPIView.as_view(),name='cdetail'),
    path('createcompany/',CreateCompanyAPIView.as_view(),name='ccreate'),
    path('updatecompany/<str:pk>/',UpdateCompanyAPIView.as_view(),name='cupdate'),
    path('deletecompany/<str:pk>/',DeleteCompanyAPIView.as_view(),name='cdelete'),

    path('',ListEmployeeAPIView.as_view(),name='employee'),
    path('detail/<str:pk>/',EmployeedetailAPIView.as_view(),name='detail'),
    path('create',CreateEmployeeAPIView.as_view(),name='create'),
    path('update/<str:pk>/',UpdateEmployeeAPIView.as_view(),name='update'),
    path('delete/<str:pk>/',DeleteEmployeeAPIView.as_view(),name='delete'),
]