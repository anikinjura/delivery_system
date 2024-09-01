# documents/models.py

from django.db import models
from core.models import Document
from reference_books.models import Agent
from registers.models import ChangeLog

class AgentDocument(Document):
    """
    Документ для создания, обновления и удаления агентов.

    Атрибуты:
        agent (ForeignKey): Агент, на которого влияет документ.
    """

    # Определение возможных типов действий
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'

    ACTION_CHOICES = [
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
    ]

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=10, choices=ACTION_CHOICES, default=CREATE)

    class Meta:
        verbose_name = "Agent Document"
        verbose_name_plural = "Agent Documents"

    def save(self, *args, **kwargs):
        """
        Переопределённый метод сохранения для реализации логики обработки документа.
        Логирует изменения в соответствующий журнал.
        """
        previous_data = {}
        if self.document_type == self.UPDATE or self.document_type == self.DELETE:
            agent = Agent.objects.get(id=self.agent.id)
            previous_data = {
                'name': agent.name,
                'description': agent.description,
                'email': agent.email,
                'phone_number': agent.phone_number,
            }

        super().save(*args, **kwargs)

        new_data = {}
        if self.document_type == self.CREATE:
            new_data = self.reference_data
        elif self.document_type == self.UPDATE:
            agent = Agent.objects.get(id=self.agent.id)
            new_data = {
                'name': agent.name,
                'description': agent.description,
                'email': agent.email,
                'phone_number': agent.phone_number,
            }
        elif self.document_type == self.DELETE:
            new_data = {}

        ChangeLog.objects.create(
            change_type=self.document_type,
            document=self,
            previous_data=previous_data,
            new_data=new_data,
            generated_by=self.user
        )
