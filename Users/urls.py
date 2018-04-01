from django.contrib import admin
from django.urls import path, include, re_path
from . import views
app_name = 'Users'
urlpatterns = [
    re_path('login/', views.login, name='login'),
    re_path('logout/', views.logout, name='logout'),
    re_path('registration/', views.registration, name='registration'),
    re_path('user_list/', views.user_list, name='user_list'),
    re_path('user_edit/(?P<user_id>[0-9]+)/$', views.user_edit, name='user_edit'),
    # re_path('user_delete/(?P<user_id>[0-9]+)/$', views.user_delete, name='user_delete'),
]