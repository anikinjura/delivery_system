# reference_books/tests.py

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Agent, PickupPoint, Employee
from datetime import date
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

class AgentModelTest(TestCase):
    """
    Тесты для модели Agent.
    Проверяет корректность создания и работы методов модели Agent.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов.
        Создает тестового агента.
        """
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="test@example.com", 
            phone_number="1234567890"
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
        self.employee = Employee.objects.create(
            user=self.user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            date_of_hire=date.today(),
            position="Manager",
            agent=self.agent
        )

    def test_employee_creation(self):
        """
        Проверяет создание сотрудника.
        Убеждается, что созданный сотрудник имеет правильные значения атрибутов.
        """
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.email, "john.doe@example.com")
        self.assertEqual(self.employee.agent, self.agent)

    def test_employee_str_method(self):
        """
        Проверяет строковое представление сотрудника.
        Убеждается, что метод __str__ возвращает правильное значение.
        """
        self.assertEqual(str(self.employee), "John  Doe - Manager")


class AgentAPITest(TestCase):
    """
    Тесты для API методов модели Agent.
    Проверяет корректность работы API для модели Agent.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов API.
        Создает тестового пользователя, токен, назначает разрешения и создает агента.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Добавляем необходимые разрешения пользователю
        manage_permission = Permission.objects.get(codename='manage_employees')
        view_permission = Permission.objects.get(codename='view_personal_data')
        self.user.user_permissions.add(manage_permission, view_permission)

        # Создаем тестового агента
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="test.agent@example.com", 
            phone_number="1234567890"
        )

    def test_agent_list(self):
        """
        Проверяет получение списка агентов через API.
        Убеждается, что запрос на получение списка агентов возвращает статус 200 и содержит данные агента.
        """
        response = self.client.get(reverse('reference_books_api:agent-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.agent.name)

    def test_agent_detail(self):
        """
        Проверяет получение деталей агента через API.
        Убеждается, что запрос на получение деталей агента возвращает статус 200 и содержит данные агента.
        """
        response = self.client.get(reverse('reference_books_api:agent-detail', args=[self.agent.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.agent.email)


class EmployeeAPITest(TestCase):
    """
    Тесты для API методов модели Employee.
    Проверяет корректность работы API для модели Employee.
    """

    def setUp(self):
        """
        Устанавливает начальные данные для тестов API.
        Создает тестового пользователя, токен, назначает разрешения и создает агента и сотрудника.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Добавляем необходимые разрешения пользователю
        manage_permission = Permission.objects.get(codename='manage_employees')
        view_permission = Permission.objects.get(codename='view_personal_data')
        self.user.user_permissions.add(manage_permission, view_permission)

        # Создаем тестового агента и сотрудника
        self.agent = Agent.objects.create(
            name="Test Agent", 
            email="test.agent@example.com", 
            phone_number="1234567890"
        )
        self.employee = Employee.objects.create(
            user=self.user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_hire=date.today(),
            position="Manager",
            agent=self.agent
        )

    def test_employee_list(self):
        """
        Проверяет получение списка сотрудников через API.
        Убеждается, что запрос на получение списка сотрудников возвращает статус 200 и содержит данные сотрудника.
        """
        response = self.client.get(reverse('reference_books_api:employee-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.email)

    def test_employee_detail(self):
        """
        Проверяет получение деталей сотрудника через API.
        Убеждается, что запрос на получение деталей сотрудника возвращает статус 200 и содержит данные сотрудника.
        """
        response = self.client.get(reverse('reference_books_api:employee-detail', args=[self.employee.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.first_name)
