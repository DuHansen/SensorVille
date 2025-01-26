# nome_do_projeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formulario.urls')),  # Incluir as URLs do app
]
