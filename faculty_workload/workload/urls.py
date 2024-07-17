from django.urls import path
from . import views
from .views import export_workload_data
from django.views.generic import TemplateView




urlpatterns = [
    path('', views.index, name='index'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('add_workload/', views.add_workload, name='add_workload'),
    path('update_workload/<int:workload_id>/', views.update_workload, name='update_workload'),
    path('delete_workload/<int:workload_id>/', views.delete_workload, name='delete_workload'),
    path('workload_table/', views.index, name='workload_table'),  # If needed
    path('export/', export_workload_data, name='export_workload_data'),
    path('visual/', TemplateView.as_view(template_name='visualization.html'), name='visual'),
    path('visualization/', views.workload_visualization, name='workload_visualization'),

    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.login_view, name='login'),
    path('sign_in/', views.sign_in_view, name='sign_in'),


]
