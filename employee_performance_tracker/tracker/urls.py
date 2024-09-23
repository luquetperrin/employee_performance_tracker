from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ServiceViewSet, GoalViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'performances', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
