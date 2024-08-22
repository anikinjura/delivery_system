# reference_books/models.py
from django.db import models
from django.contrib.auth.models import User
from core.models import ReferenceBook

class Agent(ReferenceBook):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)


    def get_pickup_points(self):
        return self.pickup_points.all()
    
    
    def __str__(self):
        return self.name
    

class PickupPoint(ReferenceBook):
    address = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, related_name='pickup_points', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(ReferenceBook):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_hire = models.DateField()
    position = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    default_pickup_point = models.ForeignKey(PickupPoint, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Добавляем дополнительные permissions (в стандартную секцию AUTHENTICATION AND AUTHORIZATION)
    class Meta:
        permissions = [
            ('manage_employees', 'Can manage employees'),
            ('view_personal_data', 'Can view personal data of employees')
        ]

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} - {self.position}"

