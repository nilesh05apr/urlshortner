from django.contrib import admin
from django.urls import path
from .views import index, upload

urlpatterns = [
    path('', upload, name='upload'),
    # path('upload',upload,name='upload')
]
