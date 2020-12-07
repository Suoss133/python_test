from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('add_book', views.add_book),

    # 显示所有主页
    path('show_books',views.show_books),
]
# app_name = 'learning_logs'
