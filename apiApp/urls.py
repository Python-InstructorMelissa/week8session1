from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
]