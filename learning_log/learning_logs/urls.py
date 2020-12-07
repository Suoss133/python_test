from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('index/', views.index),

    # 显示所有主页
    path('topics/',views.topics),
]
# app_name = 'learning_logs'
