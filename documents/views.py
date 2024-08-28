# documents/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkSchedule, WorkShift
from .forms import WorkScheduleForm, WorkShiftForm

def create_work_schedule(request):
    """
    Представление для создания графика работы.

    Если запрос POST, сохраняет данные формы и перенаправляет на список графиков.
    Иначе отображает пустую форму.
    """
    if request.method == 'POST':
        form = WorkScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = WorkScheduleForm()
    return render(request, 'documents/create_work_schedule.html', {'form': form})

def create_work_shift(request, schedule_id):
    """
    Представление для создания смены.

    Если запрос POST, проверяет данные формы на конфликт и сохраняет смену.
    """
    schedule = get_object_or_404(WorkSchedule, id=schedule_id)
    if request.method == 'POST':
        form = WorkShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.schedule = schedule
            if schedule.check_conflicts():
                shift.save()
                return redirect('schedule_detail', pk=schedule.id)
            else:
                form.add_error(None, 'Конфликт смен в расписании')
    else:
        form = WorkShiftForm(initial={'schedule': schedule})
    return render(request, 'documents/create_work_shift.html', {'form': form, 'schedule': schedule})

def approve_work_schedule(request, schedule_id):
    """
    Представление для утверждения графика работы.

    Изменяет статус графика на 'approved' и утверждает все смены.
    """
    schedule = get_object_or_404(WorkSchedule, id=schedule_id)
    schedule.approve_schedule()
    return redirect('schedule_list')
