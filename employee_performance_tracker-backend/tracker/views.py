from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import logging
from .models import User, Service, Goal, Performance
from .serializers import UserSerializer, ServiceSerializer, GoalSerializer, PerformanceSerializer, UserRegistrationSerializer

logger = logging.getLogger(__name__)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        logger.info("Received registration data: %s", request.data)  # Log incoming data
        
        # Validate and create user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This returns the newly created user object
            logger.info("User registered successfully: %s", user.username)  # Accessing username correctly
            return Response({
                "status": "success",
                "data": {
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                },
                "message": "User registered successfully."
            }, status=status.HTTP_201_CREATED)
        
        # Log and return error details
        logger.error("Registration error: %s", serializer.errors)
        return Response({
            "status": "error",
            "message": "User registration failed.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

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

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            logger.info("User logged in: %s", username)  # Log successful login
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            logger.warning("Failed login attempt for user: %s", username)  # Log failed login
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# User Profile Management
class UserProfileViewSet(viewsets.ViewSet):
    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("User updated: %s", user.username)  # Log successful update
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            logger.error("User not found: %s", pk)  # Log error if user not found
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            logger.info("User deleted: %s", user.username)  # Log successful deletion
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            logger.error("User not found: %s", pk)  # Log error if user not found
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
