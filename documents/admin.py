# documents/admin.py

from django.contrib import admin
from .models import WorkSchedule, WorkShift

admin.site.register(WorkSchedule)
admin.site.register(WorkShift)