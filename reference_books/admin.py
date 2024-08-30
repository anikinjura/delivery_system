# reference_books/admin.py
from django.contrib import admin
from .models import Agent, PickupPoint, Employee, AccountingPeriod

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Agent.
    Позволяет администратору просматривать и редактировать информацию об агентах.
    """
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    """
    Административная панель для модели PickupPoint.
    Позволяет администратору просматривать и редактировать информацию о пунктах выдачи.
    """
    list_display = ('name', 'address', 'agent', 'created_at', 'updated_at')
    list_filter = ('agent', 'created_at')
    search_fields = ('name', 'address')
    ordering = ('name',)
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Employee.
    Позволяет администратору управлять сотрудниками, фильтровать и искать по различным критериям.
    """
    list_display = ('get_full_name', 'email', 'position', 'role', 'agent', 'is_active', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'agent')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('last_name', 'first_name')
    actions = ['deactivate_employees']

    def deactivate_employees(self, request, queryset):
        """
        Деактивирует выбранных сотрудников.
        """
        queryset.update(is_active=False)
    deactivate_employees.short_description = 'Деактивировать выбранных сотрудников'


@admin.register(AccountingPeriod)
class AccountingPeriodAdmin(admin.ModelAdmin):
    """
    Административная панель для модели AccountingPeriod.
    Позволяет администратору управлять учетными периодами.
    """
    list_display = ('__str__', 'start_date', 'end_date', 'agent', 'created_at', 'updated_at')
    list_filter = ('start_date', 'end_date', 'agent')
    search_fields = ('agent__name',)
    ordering = ('-start_date',)
