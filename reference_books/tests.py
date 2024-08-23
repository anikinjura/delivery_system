# reference_books/tests.py

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Agent, PickupPoint, Employee
from datetime import date
from rest_framework.authtoken.models import Token

class AgentModelTest(TestCase):
    def setUp(self):
        self.agent = Agent.objects.create(name="Test Agent", email="test@example.com", phone_number="1234567890")

    def test_agent_creation(self):
        self.assertEqual(self.agent.name, "Test Agent")
        self.assertEqual(self.agent.email, "test@example.com")
        self.assertEqual(self.agent.phone_number, "1234567890")

    def test_agent_str_method(self):
        self.assertEqual(str(self.agent), "Test Agent")

class PickupPointModelTest(TestCase):
    def setUp(self):
        self.agent = Agent.objects.create(name="Agent 1", email="agent1@example.com", phone_number="9876543210")
        self.pickup_point = PickupPoint.objects.create(name="Pickup Point 1", address="123 Test St", agent=self.agent)

    def test_pickup_point_creation(self):
        self.assertEqual(self.pickup_point.name, "Pickup Point 1")
        self.assertEqual(self.pickup_point.address, "123 Test St")
        self.assertEqual(self.pickup_point.agent, self.agent)

    def test_pickup_point_str_method(self):
        self.assertEqual(str(self.pickup_point), "Pickup Point 1")

class EmployeeModelTest(TestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='password')

        # Создаем агента
        self.agent = Agent.objects.create(
            name="Test Agent",
            email="agent@example.com",
            phone_number="1234567890"
        )

        # Создаем сотрудника
        self.employee = Employee.objects.create(
            user=self.user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            date_of_birth="1990-01-01",
            date_of_hire=date.today(),  # Заполнение обязательного поля
            position="Manager",
            agent=self.agent
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.first_name, "John")

    def test_employee_str_method(self):
        self.assertEqual(str(self.employee), "John None Doe - Manager")

class AgentAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Аутентификация через токен
        self.agent = Agent.objects.create(name="Test Agent", email="agent@example.com", phone_number="1234567890")
        self.url = reverse('agent-detail', args=[self.agent.id])

    def test_agent_list_api(self):
        response = self.client.get(reverse('agent-list'))
        self.assertEqual(response.status_code, 200)

    def test_agent_detail_api(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Agent")

class WebInterfaceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.agent = Agent.objects.create(name="Test Agent", email="agent@example.com", phone_number="1234567890")

    def test_agents_list_view(self):
        response = self.client.get('/agents/')
        self.assertEqual(response.status_code, 200)

    def test_agent_detail_view(self):
        response = self.client.get(reverse('agent_detail', args=[self.agent.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Agent")
