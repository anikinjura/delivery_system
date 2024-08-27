# core/models.py
from django.db import models

class ReferenceBook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Это абстрактный класс, он не создаёт таблицу в базе данных

    def __str__(self):
        return self.name

class Document(models.Model):
    """
    Базовый класс для всех документов системы.

    Атрибуты:
        created_at (DateTimeField): Дата и время создания документа.
        updated_at (DateTimeField): Дата и время последнего обновления документа.
        status (CharField): Статус документа (например, 'Черновик', 'На согласовании', 'Утвержден').
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('draft', 'Черновик'),
            ('in_review', 'На согласовании'),
            ('approved', 'Утвержден'),
            ('rejected', 'Отклонен')
        ],
        default='draft'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"Document #{self.id} - {self.status}"