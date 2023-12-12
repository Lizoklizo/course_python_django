# news/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .models import Blog, News

def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    return render(request, 'news/home.html', {'latest_news': latest_news})

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog_news = News.objects.filter(blog=blog)
    return render(request, 'news/blog.html', {'blog': blog, 'blog_news': blog_news})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})

@login_required
def create_news(request):
    if request.user.is_staff:
        # Обработка формы создания новости
        return render(request, 'news/create_news.html')
    else:
        return HttpResponseForbidden()

@login_required
def edit_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.user == news.author:
        # Обработка формы редактирования новости
        return render(request, 'news/edit_news.html', {'news': news})
    else:
        return HttpResponseForbidden()

def login_view(request):
    # Обработка формы входа
    return render(request, 'news/login.html')

def register_view(request):
    # Обработка формы регистрации
    return render(request, 'news/register.html')
