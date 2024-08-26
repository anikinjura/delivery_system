# reference_books/serializers.py
from rest_framework import serializers
from .models import Agent, Employee, PickupPoint

class AgentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Agent.
    """
    class Meta:
        model = Agent
        fields = '__all__'

class PickupPointSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели PickupPoint.
    """
    agent = serializers.StringRelatedField()  # Для отображения агента в виде строки

    class Meta:
        model = PickupPoint
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Employee.
    """
    agent = serializers.StringRelatedField()  # Для отображения агента в виде строки
    default_pickup_point = serializers.StringRelatedField()  # Для отображения пункта выдачи в виде строки

    class Meta:
        model = Employee
        fields = '__all__'
