
from django.urls import path
from . views import *

urlpatterns = [
    path('',ListStudentAPIView.as_view(),name='student'),
    path('studentdetail/<int:pk>/',StudentdetailAPIView.as_view(),name='s_detail'),
    path('createstudent/',CreatestudentAPIView.as_view(),name='s_create'),
    path('updatestudent/<str:pk>/',UpdateStudentAPIView.as_view(),name='s_update'),
    path('deletestudent/<str:pk>/',DeleteStudentAPIView.as_view(),name='s_delete'),
]