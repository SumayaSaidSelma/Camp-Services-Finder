

# services/urls.py

from . import views
from django.urls import path
from .views import register

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('register/', register, name='register'),
]


