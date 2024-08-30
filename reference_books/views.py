from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Agent, Employee, PickupPoint, AccountingPeriod
from .serializers import AgentSerializer, EmployeeSerializer, PickupPointSerializer, AccountingPeriodSerializer
from rest_framework.permissions import IsAuthenticated

class AgentViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для управления объектами модели Agent.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

class PickupPointViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для управления объектами модели PickupPoint.
    """
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для управления объектами модели Employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

class AccountingPeriodViewSet(viewsets.ModelViewSet):
    """
    API ViewSet для управления объектами модели AccountingPeriod.
    """
    queryset = AccountingPeriod.objects.all()
    serializer_class = AccountingPeriodSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

def agents_list(request):
    """
    Представление для отображения списка агентов на веб-странице.
    """
    agents = Agent.objects.all()
    return render(request, 'reference_books/agents_list.html', {'agents': agents})

def agent_detail(request, pk):
    """
    Представление для отображения деталей конкретного агента.
    
    Args:
        pk (int): Первичный ключ агента.
    """
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'reference_books/agent_detail.html', {'agent': agent})

def employees_list(request):
    """
    Представление для отображения списка сотрудников на веб-странице.
    """
    employees = Employee.objects.all()
    return render(request, 'reference_books/employees_list.html', {'employees': employees})

def employee_detail(request, pk):
    """
    Представление для отображения деталей конкретного сотрудника.

    Args:
        pk (int): Первичный ключ сотрудника.
    """
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'reference_books/employee_detail.html', {'employee': employee})

def pickup_points_list(request):
    """
    Представление для отображения списка пунктов выдачи на веб-странице.
    """
    pickup_points = PickupPoint.objects.all()
    return render(request, 'reference_books/pickup_points_list.html', {'pickup_points': pickup_points})

def pickup_point_detail(request, pk):
    """
    Представление для отображения деталей конкретного пункта выдачи.

    Args:
        pk (int): Первичный ключ пункта выдачи.
    """
    pickup_point = get_object_or_404(PickupPoint, pk=pk)
    return render(request, 'reference_books/pickup_point_detail.html', {'pickup_point': pickup_point})

def accounting_periods_list(request):
    """
    Представление для отображения списка учетных периодов на веб-странице.
    """
    accounting_periods = AccountingPeriod.objects.all()
    return render(request, 'reference_books/accounting_periods_list.html', {'accounting_periods': accounting_periods})

def accounting_period_detail(request, pk):
    """
    Представление для отображения деталей конкретного учетного периода.

    Args:
        pk (int): Первичный ключ учетного периода.
    """
    accounting_period = get_object_or_404(AccountingPeriod, pk=pk)
    return render(request, 'reference_books/accounting_period_detail.html', {'accounting_period': accounting_period})
