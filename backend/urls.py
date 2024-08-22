# backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reference_books.urls')),  # Подключение маршрутов веб-интерфейса
    path('api/', include('reference_books.urls')),  # Подключение API маршрутов
]
