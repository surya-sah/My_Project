from django.urls import path
from . views import *

urlpatterns = [
    path('',ListAll.as_view(),name='All'),
    path('detail/',Employeedetail.as_view(),name='Company_detail'),
    path('create/',Createcompany.as_view(),name='Company_create'),
    path('createEmployee/',CreateEmployee.as_view(),name='Employee_create'),
    path('employeedetail/',Companywisedetail.as_view(),name='Employee_detail_companywise'),
    path('Employeedetail_all/',Employeedetail_all.as_view(),name='Employeedetail_all')

]