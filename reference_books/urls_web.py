# reference_books/urls_web.py
# Веб-маршруты для веб-интерфейса
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Для веб-части
app_name = 'reference_books_web'

urlpatterns = [
    path('agents/', views.agents_list, name='agents_list'),
    path('agents/<int:pk>/', views.agent_detail, name='agent_detail'),
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('pickup-points/', views.pickup_points_list, name='pickup_points_list'),
    path('pickup-points/<int:pk>/', views.pickup_point_detail, name='pickup_point_detail'),
    path('accounting-periods/', views.accounting_periods_list, name='accounting_periods_list'),
    path('accounting-periods/<int:pk>/', views.accounting_period_detail, name='accounting_period_detail'),
]
