
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from services import views 

urlpatterns = [
    path('admin/', admin.site.urls),
                        # Home page
    path('', views.home, name='home'),  
                        # Services URLs
    path('services/', include('services.urls')),  

                        # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='services/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

                        # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


