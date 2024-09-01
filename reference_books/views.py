# reference_books/views.py

from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticated
from .models import Agent, PickupPoint, Employee, AccountingPeriod
from .serializers import AgentSerializer, PickupPointSerializer, EmployeeSerializer, AccountingPeriodSerializer
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

class ReferenceBooksHomeView(TemplateView):
    """
    Класс представления для отображения главной страницы навигации по справочникам.
    Использует шаблон 'reference_books/base.html'.
    """
    template_name = 'reference_books/base.html'

class AgentViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для модели Agent.

    Атрибуты:
        queryset (QuerySet): Набор всех агентов.
        serializer_class (Serializer): Класс сериализатора для агента.
        permission_classes (list): Список классов разрешений.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

class PickupPointViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для модели PickupPoint.

    Атрибуты:
        queryset (QuerySet): Набор всех пунктов самовывоза.
        serializer_class (Serializer): Класс сериализатора для пункта самовывоза.
        permission_classes (list): Список классов разрешений.
    """
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для модели Employee.

    Атрибуты:
        queryset (QuerySet): Набор всех сотрудников.
        serializer_class (Serializer): Класс сериализатора для сотрудника.
        permission_classes (list): Список классов разрешений.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class AccountingPeriodViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для модели AccountingPeriod.

    Атрибуты:
        queryset (QuerySet): Набор всех учетных периодов.
        serializer_class (Serializer): Класс сериализатора для учетного периода.
        permission_classes (list): Список классов разрешений.
    """
    queryset = AccountingPeriod.objects.all()
    serializer_class = AccountingPeriodSerializer
    permission_classes = [IsAuthenticated]

def agents_list(request):
    """
    Представление для вывода списка агентов.

    Атрибуты:
        request (HttpRequest): Объект запроса.

    Возвращает:
        HttpResponse: Отображает список агентов.
    """
    agents = Agent.objects.all()
    return render(request, 'reference_books/agents_list.html', {'agents': agents})

def agent_detail(request, pk):
    """
    Представление для вывода деталей агента.

    Атрибуты:
        request (HttpRequest): Объект запроса.
        pk (int): Первичный ключ агента.

    Возвращает:
        HttpResponse: Отображает детали агента.
    """
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'reference_books/agent_detail.html', {'agent': agent})

def employees_list(request):
    """
    Представление для вывода списка сотрудников.

    Атрибуты:
        request (HttpRequest): Объект запроса.

    Возвращает:
        HttpResponse: Отображает список сотрудников.
    """
    employees = Employee.objects.all()
    return render(request, 'reference_books/employees_list.html', {'employees': employees})

def employee_detail(request, pk):
    """
    Представление для вывода деталей сотрудника.

    Атрибуты:
        request (HttpRequest): Объект запроса.
        pk (int): Первичный ключ сотрудника.

    Возвращает:
        HttpResponse: Отображает детали сотрудника.
    """
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'reference_books/employee_detail.html', {'employee': employee})

def pickup_points_list(request):
    """
    Представление для вывода списка пунктов выдачи.

    Атрибуты:
        request (HttpRequest): Объект запроса.

    Возвращает:
        HttpResponse: Отображает список пунктов выдачи.
    """
    pickup_points = PickupPoint.objects.all()
    return render(request, 'reference_books/pickup_points_list.html', {'pickup_points': pickup_points})

def pickup_point_detail(request, pk):
    """
    Представление для вывода деталей пункта выдачи.

    Атрибуты:
        request (HttpRequest): Объект запроса.
        pk (int): Первичный ключ пункта выдачи.

    Возвращает:
        HttpResponse: Отображает детали пункта выдачи.
    """
    pickup_point = get_object_or_404(PickupPoint, pk=pk)
    return render(request, 'reference_books/pickup_point_detail.html', {'pickup_point': pickup_point})

def accounting_periods_list(request):
    """
    Представление для вывода списка учетных периодов.

    Атрибуты:
        request (HttpRequest): Объект запроса.

    Возвращает:
        HttpResponse: Отображает список учетных периодов.
    """
    accounting_periods = AccountingPeriod.objects.all()
    return render(request, 'reference_books/accounting_periods_list.html', {'accounting_periods': accounting_periods})

def accounting_period_detail(request, pk):
    """
    Представление для вывода деталей учетного периода.

    Атрибуты:
        request (HttpRequest): Объект запроса.
        pk (int): Первичный ключ учетного периода.

    Возвращает:
        HttpResponse: Отображает детали учетного периода.
    """
    accounting_period = get_object_or_404(AccountingPeriod, pk=pk)
    return render(request, 'reference_books/accounting_period_detail.html', {'accounting_period': accounting_period})

@require_POST
def send_feedback(request):
    """
    Представление для обработки формы обратной связи.

    Атрибуты:
        request (HttpRequest): Объект запроса.

    Возвращает:
        HttpResponse: Перенаправляет пользователя на страницу списка агентов после отправки формы.
    """
    feedback = request.POST.get('feedback')
    # Логика обработки отзыва (например, сохранение в базе данных)
    return redirect('reference_books_web:agents_list')  # Перенаправление на страницу агентов