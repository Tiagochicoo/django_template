# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),         # Landing page
    path('register/', views.register_view, name='register'),  # Registration page
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard (login required)
]