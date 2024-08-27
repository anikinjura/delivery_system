# documents/models.py

from django.db import models
from core.models import Document
from reference_books.models import Employee, PickupPoint

class WorkSchedule(Document):
    """
    Модель, представляющая график работы сотрудника на определенный период.

    Атрибуты:
        employee (ForeignKey): Ссылка на модель Employee.
        pickup_point (ForeignKey): Ссылка на модель PickupPoint.
        start_date (DateField): Дата начала графика работы.
        end_date (DateField): Дата окончания графика работы.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def approve_schedule(self):
        """
        Метод для утверждения всех смен в графике.
        """
        for shift in self.shifts.all():
            shift.is_approved = True
            shift.save()
        self.status = 'approved'
        self.save()

    def check_conflicts(self):
        """
        Проверяет пересечения смен в рамках одного графика.
        Возвращает True, если конфликтов нет.
        """
        shifts = list(self.shifts.all())
        for i in range(len(shifts)):
            for j in range(i + 1, len(shifts)):
                if (shifts[i].date == shifts[j].date and
                    not (shifts[i].end_time <= shifts[j].start_time or shifts[j].end_time <= shifts[i].start_time)):
                    return False
        return True

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date} ({self.status})"

class WorkShift(models.Model):
    """
    Модель, представляющая смену в рамках графика работы.

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

    def approve_shift(self):
        """
        Метод для утверждения смены.
        """
        self.is_approved = True
        self.save()

    def is_conflicting(self, other_shift):
        """
        Проверяет конфликтует ли данная смена с другой.
        """
        return (self.date == other_shift.date and
                not (self.end_time <= other_shift.start_time or other_shift.end_time <= self.start_time))

    def __str__(self):
        return f"{self.employee} - {self.date} {self.start_time} to {self.end_time}"
