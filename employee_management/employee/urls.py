from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('register/', views.employee_registration, name='employee_registration'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='employee/admin_login.html'), name='login'),
    path('success/', views.success, name='success'),
path('accounts/login/', views.admin_login, name='admin_login'),
]
