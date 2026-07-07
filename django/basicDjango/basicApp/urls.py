from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_apps, name='all_apps'),
    path('<int:app_id>/', views.app_detail, name='app_detail'),
]