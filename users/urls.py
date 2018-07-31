from . import views
from django.urls import path
from django.contrib.auth import login

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_handle/', views.register_handle, name='register_handle'),
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user, name='user'),
]