from django.contrib import admin
from django.urls import path, include, re_path
from . import views
app_name = 'Users'
urlpatterns = [
    re_path('login/', views.login, name='login'),
    re_path('registration/', views.registration, name='registration'),
    re_path('admin_page/', views.admin_page, name='admin_page')
]