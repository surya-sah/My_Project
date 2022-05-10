
from django.urls import path
from . import views

urlpatterns = [
path('', views.ApiOverview, name='home'),
path('create/', views.add_items),
path('employee/add/',views.add_employee),
]
