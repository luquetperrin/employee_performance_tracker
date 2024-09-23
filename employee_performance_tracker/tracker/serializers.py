from rest_framework import serializers
from .models import User, Service, Goal, Performance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'manager']

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'description', 'target_date', 'status', 'employee', 'service']

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'update_date', 'performance_update', 'employee', 'goal']