# backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reference_books.urls_web', namespace='reference_books_web')),  # Веб-маршруты
    path('api/', include('reference_books.urls_api', namespace='reference_books_api')),  # API маршруты
]
