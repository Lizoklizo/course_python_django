# news/urls.py
from django.urls import path
from . import views  # Импортируем модуль views из текущего пакета (текущей директории)

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>/', views.blog, name='blog'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('create/', views.create_news, name='create_news'),
    path('edit/<int:news_id>/', views.edit_news, name='edit_news'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
]
