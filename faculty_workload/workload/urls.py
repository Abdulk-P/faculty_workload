from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('add_workload/', views.add_workload, name='add_workload'),
]
