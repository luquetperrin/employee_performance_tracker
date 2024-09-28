from django.contrib import admin
from django.urls import path, include
from tracker.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('tracker.urls')),
]

