# documents/forms.py

from django import forms
from .models import WorkSchedule, WorkShift

class WorkScheduleForm(forms.ModelForm):
    class Meta:
        model = WorkSchedule
        fields = ['employee', 'pickup_point', 'start_date', 'end_date']

class WorkShiftForm(forms.ModelForm):
    class Meta:
        model = WorkShift
        fields = ['schedule', 'employee', 'date', 'start_time', 'end_time']
