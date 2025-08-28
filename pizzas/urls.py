"""Defines URL patterns for pizzas"""
from django.urls import path        # build URL paths and map URLs to views
from . import views                 # retrieved data and send it back with template

app_name = 'pizzas'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page with Menu of pizzas
    path('pizzas/', views.pizzas, name = 'pizzas_menu' ),
]