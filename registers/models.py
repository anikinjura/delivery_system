# registers/models.py

from django.db import models
from documents.models import WorkSchedule, WorkShift

class WorkScheduleRegister(models.Model):
    """
    Модель регистра, представляющая журнал изменений графиков работы.

    Атрибуты:
        work_schedule (ForeignKey): Ссылка на график работы.
        change_date (DateTimeField): Дата и время изменения.
        status (CharField): Статус графика после изменения.
        comment (TextField): Комментарий к изменению.
    """
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    change_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.work_schedule} - {self.status} on {self.change_date}"
