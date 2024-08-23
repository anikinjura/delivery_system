# reference_books/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (AgentViewSet, EmployeeViewSet, PickupPointViewSet,
                    agents_list, agent_detail, employees_list, employee_detail,
                    pickup_points_list, pickup_point_detail)

# Создаем роутер для API ViewSets
router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'pickup-points', PickupPointViewSet)

urlpatterns = [
    # API Routes
    path('api/', include(router.urls)),  # Все API маршруты начинаются с api/

    # Web Interface Routes
    path('agents/', agents_list, name='agents_list'),  # Список агентов
    path('agents/<int:pk>/', agent_detail, name='agent_detail'),  # Детали агента
    path('employees/', employees_list, name='employees_list'),  # Список сотрудников
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),  # Детали сотрудника
    path('pickup-points/', pickup_points_list, name='pickup_points_list'),  # Список пунктов выдачи
    path('pickup-points/<int:pk>/', pickup_point_detail, name='pickup_point_detail'),  # Детали пункта выдачи
]
