from django.contrib import admin
from .models import User, Service, Goal, Performance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('description', 'target_date', 'status', 'employee', 'service')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('update_date', 'performance_update', 'employee', 'goal')