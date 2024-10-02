

from django.urls import path
from . import views
from .views import ServiceUpdateView, ServiceDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.service_list, name='service_list'),  
    path('service/<int:pk>/', login_required(views.service_detail), name='service_detail'),
    path('service/<int:pk>/edit/', login_required(ServiceUpdateView.as_view()), name='service_update'),  # Edit Service
    path('service/<int:pk>/delete/', login_required(ServiceDeleteView.as_view()), name='service_delete'),  # Delete Service
    path('service/new/', login_required(views.create_service), name='create_service'),
    path('service/add/', login_required(views.add_service), name='add_service'),
]
