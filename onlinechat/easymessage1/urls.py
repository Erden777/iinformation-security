
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chat_id>/', views.chat_details, name='details'),
    path('login/', views.login, name='login')
]
