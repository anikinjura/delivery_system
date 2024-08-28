# reports/views.py

from django.shortcuts import render
from documents.models import WorkShift
from .models import WorkScheduleReport
from reference_books.models import Employee
from django.utils import timezone
from datetime import timedelta

def generate_work_schedule_report(request, employee_id):
    """
    Представление для генерации отчета по графику работы.

    Генерирует отчет по отработанным часам и утвержденным сменам для сотрудника.
    """
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    start_period = today - timedelta(days=30)  # отчет за последние 30 дней
    shifts = WorkShift.objects.filter(employee=employee, date__range=(start_period, today), is_approved=True)

    total_hours = sum((shift.end_time.hour - shift.start_time.hour) for shift in shifts)
    approved_shifts_count = shifts.count()

    report = WorkScheduleReport.objects.create(
        employee=employee,
        report_date=today,
        total_hours=total_hours,
        approved_shifts=approved_shifts_count
    )

    return render(request, 'reports/work_schedule_report.html', {'report': report})
