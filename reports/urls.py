# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate_report/<int:employee_id>/', views.generate_work_schedule_report, name='generate_report'),
]