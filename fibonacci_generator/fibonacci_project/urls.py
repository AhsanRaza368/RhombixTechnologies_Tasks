from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fibonacci_app.urls')),  # Include the app's URLs
]
