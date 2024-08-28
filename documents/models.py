# documents/models.py

from django.db import models
from core.models import Document
from reference_books.models import Employee, PickupPoint

class WorkSchedule(Document):
    """
    Модель, представляющая график работы сотрудников.

    Атрибуты:
        employee (ForeignKey): Ссылка на сотрудника, для которого создается график.
        pickup_point (ForeignKey): Ссылка на пункт выдачи, связанный с графиком.
        start_date (DateField): Дата начала учетного периода.
        end_date (DateField): Дата окончания учетного периода.
        status (CharField): Статус графика (на утверждении, утверждено, отклонено).
    """
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('on_approval', 'На утверждении'),
        ('approved', 'Утверждено'),
        ('rejected', 'Отклонено'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date} ({self.status})"
    
    def approve_schedule(self):
        """
        Утверждает все смены в графике. Изменяет статус графика на 'approved'.
        """
        for shift in self.shifts.all():
            shift.is_approved = True
            shift.save()
        self.status = 'approved'
        self.save()

    def reject_schedule(self):
        """
        Отклоняет график. Изменяет статус графика на 'rejected'.
        """
        self.status = 'rejected'
        self.save()

    def check_conflicts(self):
        """
        Проверяет пересечения смен в графике.
        Возвращает True, если конфликтов нет.
        """
        shifts = list(self.shifts.all())
        for i in range(len(shifts)):
            for j in range(i + 1, len(shifts)):
                if (shifts[i].date == shifts[j].date and
                    not (shifts[i].end_time <= shifts[j].start_time or shifts[j].end_time <= shifts[i].start_time)):
                    return False
        return True


class WorkShift(Document):
    """
    Модель, представляющая смену в графике работы.

    Атрибуты:
        schedule (ForeignKey): Ссылка на график работы, к которому относится смена.
        employee (ForeignKey): Сотрудник, выполняющий смену.
        date (DateField): Дата смены.
        start_time (TimeField): Время начала смены.
        end_time (TimeField): Время окончания смены.
        is_approved (BooleanField): Статус утверждения смены.
    """
    schedule = models.ForeignKey(WorkSchedule, related_name='shifts', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.date} {self.start_time} to {self.end_time}"
    
    def approve_shift(self):
        """
        Утверждает смену.
        """
        self.is_approved = True
        self.save()

    def is_conflicting(self, other_shift):
        """
        Проверяет, конфликтует ли данная смена с другой.
        """
        return (self.date == other_shift.date and
                not (self.end_time <= other_shift.start_time or other_shift.end_time <= self.start_time))
