# backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Веб-интерфейс
    path('reference_books/', include('reference_books.urls_web', namespace='reference_books_web')),
    path('documents/', include('documents.urls_web', namespace='documents_web')),

    # API
    path('api/reference_books/', include('reference_books.urls_api', namespace='reference_books_api')),
    path('api/documents/', include('documents.urls_api', namespace='documents_api')),
]
