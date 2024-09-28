from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('manager', 'Manager'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username  # Added for better representation


class Service(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_services')

    def __str__(self):
        return self.name


class Goal(models.Model):
    description = models.TextField()
    target_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ])
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='goals')

    def __str__(self):
        return self.description


class Performance(models.Model):
    update_date = models.DateField()
    performance_update = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performances')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='performances')

    def __str__(self):
        return f"{self.employee.username} - {self.goal.description}"
