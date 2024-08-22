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
