# registers/models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from core.models import Report

class ChangeLog(Report):
    """
    Лог изменений для документов системы, наследует базовый класс Report.
    
    Атрибуты:
        document_type (ForeignKey): Тип документа, указывающий на модель, к которой относится запись.
        document_id (PositiveIntegerField): ID документа.
        document (GenericForeignKey): Ссылка на конкретный документ.
        user (ForeignKey): Пользователь, который внёс изменения.
        action (CharField): Действие, совершённое пользователем (создание, изменение, удаление).
        timestamp (DateTimeField): Время выполнения действия.
    """
    document_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    document_id = models.PositiveIntegerField()
    document = GenericForeignKey('document_type', 'document_id')
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='action_logs'  # Уникальное имя для обратной связи
    )
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Change Log"
        verbose_name_plural = "Change Logs"

    def __str__(self):
        return f"ChangeLog for {self.document_type} #{self.document_id} by {self.user} on {self.timestamp}"
