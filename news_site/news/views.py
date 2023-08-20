from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)
    # return HttpResponse('Hello world')

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def view_news(request, news_id):
    """Подключаем кнопку Read more"""
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})