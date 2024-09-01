# documents/serializers.py

from rest_framework import serializers
from .models import AgentDocument

class AgentDocumentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели AgentDocument.

    Атрибуты:
        id (IntegerField): Идентификатор документа.
        document_type (CharField): Тип документа (создание, обновление, удаление).
        reference_data (JSONField): Данные, которые документ фиксирует.
        status (CharField): Статус документа.
        agent (IntegerField): Идентификатор агента.
    """
    class Meta:
        model = AgentDocument
        fields = ['id', 'document_type', 'reference_data', 'status', 'agent', 'user', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
