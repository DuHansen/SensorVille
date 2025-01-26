from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.formulario_view, name='formulario'),
    path('sucesso/', lambda request: render(request, 'sucesso.html'), name='sucesso'),
]
