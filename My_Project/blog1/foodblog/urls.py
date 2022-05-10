
from django.urls import path
from . views import *

urlpatterns = [
    path('',ListPostAPIView.as_view(),name='post'),
    path('postdetail/<str:pk>/',PostdetailAPIView.as_view(),name='detail'),
    path('createpost/',CreatePostAPIView.as_view(),name='create'),
    path('updatepost/<str:pk>/',UpdatePostAPIView.as_view(),name='update'),
    path('deletepost<str:pk>/',DeletePostAPIView.as_view(),name='delete'),
]   