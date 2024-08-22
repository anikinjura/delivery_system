# reference_books/admin.py
from django.contrib import admin
from .models import Agent, PickupPoint, Employee

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'agent', 'created_at', 'updated_at')
    list_filter = ('agent',)
    search_fields = ('name',)
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'position', 'agent', 'is_active')
    list_filter = ('default_pickup_point', 'agent')
    search_fields = ('first_name', 'middle_name', 'last_name', 'email')