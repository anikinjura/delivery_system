# reference_books/urls_api.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reference_books_api'

# Регистрация маршрутов API с использованием DefaultRouter
router = DefaultRouter()
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'employees', views.EmployeeViewSet, basename='employee')
router.register(r'pickup-points', views.PickupPointViewSet, basename='pickuppoint')
router.register(r'accounting-periods', views.AccountingPeriodViewSet, basename='accountingperiod')

urlpatterns = [
    # Включение маршрутов, зарегистрированных в router
    path('', include(router.urls)),
]
