from django.contrib import admin
from django.urls import path
from .views import index, reroute, upload

urlpatterns = [
    path('', upload, name='upload'),
    path('<str:pk>',reroute,name='reroute')
]
