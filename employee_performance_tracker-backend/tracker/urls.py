from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ServiceViewSet, GoalViewSet, PerformanceViewSet, UserRegistrationView, LoginView, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'performances', PerformanceViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='user-login'),  # Added login path
    path('users/<int:pk>/profile/', UserProfileViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='user-profile'),  # Added user profile management paths
    path('', include(router.urls)),
]
