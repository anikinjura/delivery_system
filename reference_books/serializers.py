# reference_books/serializers.py

from rest_framework import serializers
from .models import Agent, Employee, PickupPoint, AccountingPeriod

class AgentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Agent.

    Атрибуты:
        name (CharField): Имя агента.
        email (EmailField): Email агента.
        phone_number (CharField): Номер телефона агента.
    """
    class Meta:
        model = Agent
        fields = '__all__'

class PickupPointSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели PickupPoint.

    Атрибуты:
        name (CharField): Имя пункта самовывоза.
        address (CharField): Адрес пункта самовывоза.
        agent (RelatedField): Агент, связанный с пунктом самовывоза.
    """
    agent = serializers.StringRelatedField()

    class Meta:
        model = PickupPoint
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Employee.

    Атрибуты:
        first_name (CharField): Имя сотрудника.
        last_name (CharField): Фамилия сотрудника.
        email (EmailField): Email сотрудника.
        phone_number (CharField): Номер телефона сотрудника.
        position (CharField): Должность сотрудника.
        role (CharField): Роль сотрудника.
        agent (RelatedField): Агент, связанный с сотрудником.
        default_pickup_point (RelatedField): Пункт выдачи сотрудника по умолчанию.
    """
    agent = serializers.StringRelatedField()
    default_pickup_point = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = '__all__'

class AccountingPeriodSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели AccountingPeriod.

    Атрибуты:
        agent (RelatedField): Агент, связанный с учетным периодом.
        start_date (DateField): Дата начала учетного периода.
        end_date (DateField): Дата окончания учетного периода.
    """
    agent = serializers.StringRelatedField()

    class Meta:
        model = AccountingPeriod
        fields = '__all__'
