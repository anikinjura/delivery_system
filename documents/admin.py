# documents/admin.py

from django.contrib import admin
from .models import AgentDocument

@admin.register(AgentDocument)
class AgentDocumentAdmin(admin.ModelAdmin):
    """
    Админка для управления документами AgentDocument.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке документов.
        search_fields (tuple): Поля для поиска по документам.
    """
    list_display = ('document_type', 'agent', 'status', 'created_at', 'updated_at')
    search_fields = ('agent__name', 'status')
