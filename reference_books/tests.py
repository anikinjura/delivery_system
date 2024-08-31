# reference_books/tests.py

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Agent, PickupPoint, Employee, AccountingPeriod
from datetime import date
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from django.utils import timezone

class AgentModelTest(TestCase):
    """
    Тесты для модели Agent.
    Проверяет корректность создания и работы методов модели Agent.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов.
        Создает тестового агента и несколько пунктов выдачи.
        """
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="test@example.com", 
            phone_number="1234567890"
        )
        self.pickup_point_1 = PickupPoint.objects.create(
            name="Pickup Point 1", 
            address="123 Test St", 
            agent=self.agent
        )
        self.pickup_point_2 = PickupPoint.objects.create(
            name="Pickup Point 2", 
            address="456 Test Ave", 
            agent=self.agent
        )

    def test_agent_creation(self):
        """
        Проверяет создание агента.
        Убеждается, что созданный агент имеет правильные значения атрибутов.
        """
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.email, "test@example.com")
        self.assertEqual(self.agent.phone_number, "1234567890")

    def test_agent_str_method(self):
        """
        Проверяет строковое представление агента.
        Убеждается, что метод __str__ возвращает правильное значение.
        """
        self.assertEqual(str(self.agent), "Test Agent")

    def test_agent_get_pickup_points(self):
        """
        Проверяет метод get_pickup_points.
        Убеждается, что метод возвращает правильный набор пунктов выдачи.
        """
        pickup_points = self.agent.get_pickup_points()
        self.assertIn(self.pickup_point_1, pickup_points)
        self.assertIn(self.pickup_point_2, pickup_points)


class PickupPointModelTest(TestCase):
    """
    Тесты для модели PickupPoint.
    Проверяет корректность создания и работы методов модели PickupPoint.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов.
        Создает тестового агента и пункт выдачи.
        """
        self.agent = Agent.objects.create(
            name="Agent 1", 
            email="agent1@example.com", 
            phone_number="9876543210"
        )
        self.pickup_point = PickupPoint.objects.create(
            name="Pickup Point 1", 
            address="123 Test St", 
            agent=self.agent
        )

    def test_pickup_point_creation(self):
        """
        Проверяет создание пункта выдачи.
        Убеждается, что созданный пункт выдачи имеет правильные значения атрибутов.
        """
        self.assertEqual(self.pickup_point.name, "Pickup Point 1")
        self.assertEqual(self.pickup_point.address, "123 Test St")
        self.assertEqual(self.pickup_point.agent, self.agent)

    def test_pickup_point_str_method(self):
        """
        Проверяет строковое представление пункта выдачи.
        Убеждается, что метод __str__ возвращает правильное значение.
        """
        self.assertEqual(str(self.pickup_point), "Pickup Point 1")


class EmployeeModelTest(TestCase):
    """
    Тесты для модели Employee.
    Проверяет корректность создания и работы методов модели Employee.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов.
        Создает тестового пользователя, агента и сотрудника.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="agent@example.com", 
            phone_number="1234567890"
        )
        self.pickup_point = PickupPoint.objects.create(
            name="Pickup Point 1", 
            address="123 Test St", 
            agent=self.agent
        )
        self.employee = Employee.objects.create(
            user=self.user,
            first_name="John",
            middle_name="Middle",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            date_of_hire=date.today(),
            position="Manager",
            role="manager",
            agent=self.agent,
            default_pickup_point=self.pickup_point,
            is_active=True
        )

    def test_employee_creation(self):
        """
        Проверяет создание сотрудника.
        Убеждается, что созданный сотрудник имеет правильные значения атрибутов.
        """
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.middle_name, "Middle")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.email, "john.doe@example.com")
        self.assertEqual(self.employee.agent, self.agent)
        self.assertEqual(self.employee.default_pickup_point, self.pickup_point)

    def test_employee_str_method(self):
        """
        Проверяет строковое представление сотрудника.
        Убеждается, что метод __str__ возвращает правильное значение.
        """
        self.assertEqual(str(self.employee), "John Middle Doe - Manager")

    def test_employee_get_full_name(self):
        """
        Проверяет метод get_full_name.
        Убеждается, что метод возвращает правильное полное имя сотрудника.
        """
        full_name = self.employee.get_full_name()
        self.assertEqual(full_name, "Doe John Middle")

    def test_employee_deactivate(self):
        """
        Проверяет метод deactivate.
        Убеждается, что метод корректно деактивирует сотрудника.
        """
        self.employee.deactivate()
        self.assertFalse(self.employee.is_active)


class AccountingPeriodModelTest(TestCase):
    """
    Тесты для модели AccountingPeriod.
    Проверяет корректность создания и работы методов модели AccountingPeriod.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов.
        Создает тестового агента и учетный период.
        """
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="agent@example.com", 
            phone_number="1234567890"
        )
        self.accounting_period = AccountingPeriod.objects.create(
            agent=self.agent,
            start_date=date(2023, 1, 1),
            end_date=date(2023, 12, 31)
        )

    def test_accounting_period_creation(self):
        """
        Проверяет создание учетного периода.
        Убеждается, что созданный учетный период имеет правильные значения атрибутов.
        """
        self.assertEqual(self.accounting_period.agent, self.agent)
        self.assertEqual(self.accounting_period.start_date, date(2023, 1, 1))
        self.assertEqual(self.accounting_period.end_date, date(2023, 12, 31))

    def test_accounting_period_str_method(self):
        """
        Проверяет строковое представление учетного периода.
        Убеждается, что метод __str__ возвращает правильное значение.
        """
        self.assertEqual(str(self.accounting_period), "Учетный период: 2023-01-01 - 2023-12-31 (Test Agent)")

    def test_accounting_period_is_active(self):
        """
        Проверяет метод is_active.
        Убеждается, что метод корректно определяет активность учетного периода.
        """
        today = timezone.now().date()
        active_period = AccountingPeriod.objects.create(
            agent=self.agent,
            start_date=today,
            end_date=today
        )
        self.assertTrue(active_period.is_active())

        past_period = AccountingPeriod.objects.create(
            agent=self.agent,
            start_date=date(2022, 1, 1),
            end_date=date(2022, 12, 31)
        )
        self.assertFalse(past_period.is_active())

