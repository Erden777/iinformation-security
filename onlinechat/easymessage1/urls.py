
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('<int:chat_id>/', views.check_password, name='check_password'),
    path('<int:chat_id>/details/', views.chat_details, name='details'),
    path('save/', views.save_message, name='post_message'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.singin, name='singin')
]
