from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_handle/', views.register_handle, name='register_handle'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user, name='user'),
]