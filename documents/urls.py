# documents/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_schedule/', views.create_work_schedule, name='create_schedule'),
    path('create_shift/<int:schedule_id>/', views.create_work_shift, name='create_shift'),
    path('approve_schedule/<int:schedule_id>/', views.approve_work_schedule, name='approve_schedule'),
]
