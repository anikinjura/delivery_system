# reference_books/models.py

from django.db import models
from django.contrib.auth.models import User
from core.models import ReferenceBook

class Agent(ReferenceBook):
    """
    Справочник Agent представляет агента - влыдельца пунктов выдачи

    Атрибуты:
        email (EmailField): Уникальный email агента.
        phone_number (CharField): Уникальный номер телефона агента.
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def get_pickup_points(self):
        """
        Возвращает все пункты выдачи, связанные с агентом.

        Возвращает:
            QuerySet: Набор пунктов выдачи, связанных с агентом.
        """
        return self.pickup_points.all()
    
    def __str__(self):
        return self.name
    

class PickupPoint(ReferenceBook):
    """
    Справочник PickupPoint представляет пункт выдачи, связанный с агентом.

    Атрибуты:
        address (CharField): Адрес пункта выдачи.
        agent (ForeignKey): Связь с моделью Agent.
    """
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, related_name='pickup_points', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(ReferenceBook):
    """
    Справочник Employee представляет сотрудника, связанного с агентом, и содержит его личную информацию.

    Атрибуты:
        user (OneToOneField): Пользователь, связанный с сотрудником.
        first_name (CharField): Имя сотрудника.
        middle_name (CharField): Отчество сотрудника (необязательно).
        last_name (CharField): Фамилия сотрудника.
        email (EmailField): Уникальный email сотрудника.
        phone_number (CharField): Номер телефона сотрудника (необязательно).
        date_of_birth (DateField): Дата рождения сотрудника.
        date_of_hire (DateField): Дата найма сотрудника.
        position (CharField): Должность сотрудника.
        role (CharField): Роль сотрудника (employee, manager, admin).
        agent (ForeignKey): Агент, с которым связан сотрудник.
        default_pickup_point (ForeignKey): Пункт выдачи по умолчанию (необязательно).
        is_active (BooleanField): Статус активности сотрудника.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_hire = models.DateField()
    position = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50,
        choices=[
            ('employee', 'Employee'),
            ('manager', 'Manager'),
            ('admin', 'Administrator')
        ],
        default='employee'
    )    
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    default_pickup_point = models.ForeignKey(PickupPoint, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        permissions = [
            ('manage_employees', 'Can manage employees'),
            ('view_personal_data', 'Can view personal data of employees')
        ]

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name} - {self.position}"

    def get_full_name(self):
        """
        Возвращает полное имя сотрудника в формате "Фамилия Имя Отчество".

        Возвращает:
            str: Фамилия Имя Отчество.
        """
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    def deactivate(self):
        """
        Деактивирует сотрудника, устанавливая флаг is_active в False.
        """
        self.is_active = False
        self.save()


class AccountingPeriod(ReferenceBook):
    """
    Справочник AccountingPeriod представляет учетный период, связанный с агентом.
    Предназначен для ведения учета расчета зарплаты сотрудникам в пределах используемого Агентом учетного периода
    В пределах учетного периода ведется фиксация таких показателей как:
    1. количество отработанных часов сотрудниками в разрезе дней
    2. количество опозданий в разрезе дней
    3. количество выдач посылок с пункта выдачи в разрезе дней
    Эти показатели в дальнейшем используются для расчета зарплаты за отработанные часы а так-же стимулирующих выплат в пределах учетного периода
    Атрибуты:
        agent (ForeignKey): Агент, связанный с учетным периодом.
        start_date (DateField): Дата начала учетного периода.
        end_date (DateField): Дата окончания учетного периода.
    """
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Учетный период: {self.start_date} - {self.end_date} ({self.agent})"

    def is_active(self):
        """
        Проверяет, активен ли учетный период на текущую дату.

        Возвращает:
            bool: True, если учетный период активен, иначе False.
        """
        from django.utils import timezone
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
