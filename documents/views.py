# documents/views.py

from rest_framework import viewsets
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import AgentDocument
from .forms import AgentDocumentForm
from .serializers import AgentDocumentSerializer
from django.views.generic import TemplateView
from reference_books.models import Agent

class DocumentHomeView(TemplateView):
    """
    Класс представления для отображения главной страницы навигации по документам.
    Использует шаблон 'documents/base.html'.
    """
    template_name = 'documents/base.html'

class AgentDocumentViewSet(viewsets.ModelViewSet):
    """
    API для работы с документами AgentDocument.

    Атрибуты:
        queryset (QuerySet): Список документов.
        serializer_class (Serializer): Сериализатор для модели AgentDocument.
    """
    queryset = AgentDocument.objects.all()
    serializer_class = AgentDocumentSerializer

    def perform_create(self, serializer):
        """
        Сохранение объекта с указанием текущего пользователя.
        """
        serializer.save(user=self.request.user)

class AgentDocumentWebView(View):
    """
    Веб-интерфейс для работы с документами AgentDocument.
    """
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            document = get_object_or_404(AgentDocument, pk=kwargs['pk'])
            return render(request, 'documents/agent_documents/agent_document_detail.html', {'document': document})
        else:
            documents = AgentDocument.objects.all()
            return render(request, 'documents/agent_documents/agent_document_list.html', {'documents': documents})

    def post(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            document = get_object_or_404(AgentDocument, pk=kwargs['pk'])
            form = AgentDocumentForm(request.POST, instance=document)
        else:
            form = AgentDocumentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('documents_web:agent_document_list')
        
        return render(request, 'documents/agent_documents/agent_document_form.html', {'form': form})
