# documents/urls_web.py

from django.urls import path
from .views import AgentDocumentWebView, DocumentHomeView

app_name = 'documents_web'

urlpatterns = [
    path('', DocumentHomeView.as_view(), name='document_home'),
    # Главная страница навигации по документам. Включает ссылки на другие документы и разделы.

    path('agent-documents/', AgentDocumentWebView.as_view(), name='agent_document_list'),
    # Маршрут для отображения списка документов агентов

    path('agent-documents/create/', AgentDocumentWebView.as_view(), name='agent_document_form'),
    # Маршрут для создания нового документа агента

    path('agent-documents/<int:pk>/', AgentDocumentWebView.as_view(), name='agent_document_detail'),
    # Маршрут для просмотра деталей конкретного документа агента

    path('agent-documents/<int:pk>/edit/', AgentDocumentWebView.as_view(), name='agent_document_form'),
    # Маршрут для редактирования существующего документа агента

    path('agent-documents/<int:pk>/delete/', AgentDocumentWebView.as_view(), name='agent_document_delete'),
    # Маршрут для удаления существующего документа агента
]
