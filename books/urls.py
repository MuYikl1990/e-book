from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:books_id>/', views.detail, name='detail'),
    path('list/<int:type_id>/<int:page>/', views.list, name='list'),
]