# documents/urls_api.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentDocumentViewSet

app_name = 'documents_api'

router = DefaultRouter()
router.register(r'agent-documents', AgentDocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
