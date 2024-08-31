# reference_books/admin.py

from django.contrib import admin
from .models import Agent, PickupPoint, Employee, AccountingPeriod

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели Agent с настройками отображения, фильтрации и поиска.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке агентов.
        search_fields (tuple): Поля для поиска агентов.
        list_filter (tuple): Поля для фильтрации агентов.
        ordering (tuple): Поля для сортировки агентов.
    """
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели PickupPoint с настройками отображения, фильтрации и поиска.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке пунктов самовывоза.
        list_filter (tuple): Поля для фильтрации пунктов самовывоза.
        search_fields (tuple): Поля для поиска пунктов самовывоза.
        ordering (tuple): Поля для сортировки пунктов самовывоза.
    """
    list_display = ('name', 'address', 'agent', 'created_at', 'updated_at')
    list_filter = ('agent', 'created_at')
    search_fields = ('name', 'address')
    ordering = ('name',)
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели Employee с настройками отображения, фильтрации и поиска.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке сотрудников.
        list_filter (tuple): Поля для фильтрации сотрудников.
        search_fields (tuple): Поля для поиска сотрудников.
        ordering (tuple): Поля для сортировки сотрудников.
        actions (list): Список доступных действий в админке.
    """
    list_display = ('get_full_name', 'email', 'position', 'role', 'agent', 'is_active', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'agent')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('last_name', 'first_name')
    actions = ['deactivate_employees']

    def deactivate_employees(self, request, queryset):
        """
        Админ-действие для деактивации выбранных сотрудников.

        Аргументы:
            request (HttpRequest): Объект запроса.
            queryset (QuerySet): Набор объектов, выбранных для действия.

        Действие:
            Обновляет статус is_active на False для всех выбранных сотрудников.
        """
        queryset.update(is_active=False)
    deactivate_employees.short_description = 'Деактивировать выбранных сотрудников'


@admin.register(AccountingPeriod)
class AccountingPeriodAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели AccountingPeriod с настройками отображения, фильтрации и поиска.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке учетных периодов.
        list_filter (tuple): Поля для фильтрации учетных периодов.
        search_fields (tuple): Поля для поиска учетных периодов.
        ordering (tuple): Поля для сортировки учетных периодов.
    """
    list_display = ('__str__', 'start_date', 'end_date', 'agent', 'created_at', 'updated_at')
    list_filter = ('start_date', 'end_date', 'agent')
    search_fields = ('agent__name',)
    ordering = ('-start_date',)
