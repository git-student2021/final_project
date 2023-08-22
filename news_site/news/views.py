from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #нет доступа если Не авторизован
from django.core.paginator import Paginator

#from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num) # get_page остаемся на последней странице если номер не существует
    return render(request, 'news/test.html', {'page_obj': page_objects})




class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'  # указываем с каким шаблонам будем работать (news_list.html по умолчанию)
    context_object_name = 'news' # # указываем с каким объектом будем работать (object_list по умолчанию)
    # extra_context = {'title': ' Главная'}
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)
#     # return HttpResponse('Hello world')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'  # указываем с каким шаблонам будем работать (news_list.html по умолчанию)
    context_object_name = 'news'  # # указываем с каким объектом будем работать (object_list по умолчанию)
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})



class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'  # указываем с каким шаблонам будем работать

# def view_news(request, news_id):
#     """Подключаем кнопку Read more"""
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id) # если стрпницы нет то на выходе 404 ошибка
#     return render(request, 'news/view_news.html', {"news_item": news_item})


class CreateNews(LoginRequiredMixin, CreateView): # LoginRequiredMixin нет доступа если Не авторизован
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home') # redirect на главную страницу
    raise_exception = True

# def add_news(request):
#     """Подключаем Добавить новость на главной странице, форма не связана с моделью"""
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news = News.objects.create(**form.cleaned_data)
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})

# def add_news(request):
#     """Подключаем Добавить новость на главной странице, форма связана с моделью"""
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})