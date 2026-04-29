from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chatbot, name='chatbot'),
    path('diet/', views.diet, name='diet'),
    path('profile/', views.profile, name='profile'),
]
