# reports/models.py

from django.db import models
from reference_books.models import Employee

class WorkScheduleReport(models.Model):
    """
    Модель для отчетов по графикам работы.

    Атрибуты:
        employee (ForeignKey): Ссылка на сотрудника, для которого создается отчет.
        report_date (DateField): Дата создания отчета.
        total_hours (DecimalField): Общее количество отработанных часов.
        approved_shifts (IntegerField): Количество утвержденных смен.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    report_date = models.DateField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    approved_shifts = models.IntegerField()

    def __str__(self):
        return f"Отчет {self.employee} за {self.report_date}"
