# reference_books/urls_api.py
# API-маршруты для API
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reference_books_api'

router = DefaultRouter()
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'employees', views.EmployeeViewSet, basename='employee')
router.register(r'pickup-points', views.PickupPointViewSet, basename='pickuppoint')
router.register(r'accounting-periods', views.AccountingPeriodViewSet, basename='accountingperiod')

urlpatterns = [
    path('', include(router.urls)),
]
