

from django.urls import path
from . import views
from .views import ServiceUpdateView, ServiceDeleteView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLogoutView

urlpatterns = [
    path('', views.service_list, name='service_list'),  
    path('service/<int:pk>/', login_required(views.service_detail), name='service_detail'),
    path('services/service/<int:pk>/edit/', ServiceUpdateView.as_view(), name='edit_service'),
    path('services/service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete_service'),
    path('service/new/', login_required(views.create_service), name='create_service'),
    path('service/add/', login_required(views.add_service), name='add_service'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


