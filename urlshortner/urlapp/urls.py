from django.contrib import admin
from django.urls import path
from .views import reroute,api,health

urlpatterns = [
    path('health/',health),
    path('', api, name='api'),
    path('<str:pk>',reroute,name='reroute')
]
