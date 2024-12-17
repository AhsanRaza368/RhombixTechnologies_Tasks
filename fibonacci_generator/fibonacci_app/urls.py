from django.urls import path
from .views import fibonacci_view

urlpatterns = [
    path('', fibonacci_view, name='fibonacci'),
]
