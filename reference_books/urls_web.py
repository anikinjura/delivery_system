# reference_books/urls_web.py

from django.urls import path
from . import views

app_name = 'reference_books_web'

urlpatterns = [
    # Маршруты для агентов
    path('agents/', views.agents_list, name='agents_list'),
    path('agents/<int:pk>/', views.agent_detail, name='agent_detail'),
    
    # Маршруты для сотрудников
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    
    # Маршруты для пунктов самовывоза
    path('pickup-points/', views.pickup_points_list, name='pickup_points_list'),
    path('pickup-points/<int:pk>/', views.pickup_point_detail, name='pickup_point_detail'),
    
    # Маршруты для учетных периодов
    path('accounting-periods/', views.accounting_periods_list, name='accounting_periods_list'),
    path('accounting-periods/<int:pk>/', views.accounting_period_detail, name='accounting_period_detail'),

    # Маршрут для отправки обратной связи
    path('send_feedback/', views.send_feedback, name='send_feedback'),    
]
