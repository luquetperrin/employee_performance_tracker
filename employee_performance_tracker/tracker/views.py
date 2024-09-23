from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Service, Goal, Performance
from .serializers import UserSerializer, ServiceSerializer, GoalSerializer, PerformanceSerializer

def home(request):
    return HttpResponse("Welcome to the Employee Performance Tracker!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer