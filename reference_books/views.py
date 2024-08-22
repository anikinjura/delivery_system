# reference_books/views.py
from rest_framework import viewsets
from .models import Agent, Employee, PickupPoint
from .serializers import AgentSerializer, EmployeeSerializer, PickupPointSerializer
from django.shortcuts import render, get_object_or_404

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class PickupPointViewSet(viewsets.ModelViewSet):
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def agents_list(request):
    agents = Agent.objects.all()
    return render(request, 'reference_books/agents_list.html', {'agents': agents})

def agent_detail(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'reference_books/agent_detail.html', {'agent': agent})