# config/urls.py

# Import from django modules
from django.contrib import admin
from django.urls import path, include

# Import from locals

urlpatterns = [
    # sekdilu139
    path('', include('apps.sekdilu139.urls', namespace='sekdilu139')),
    path('admin/', admin.site.urls),
]
