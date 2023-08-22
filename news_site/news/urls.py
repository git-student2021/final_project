from django.urls import path

from .views import    HomeNews, NewsByCategory, ViewNews, CreateNews, test, register, login
# index, get_category, view_news, add_news,
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('test/', test, name='test'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'), # Подключаем кнопку Read more
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'), # Подключаем кнопку Read more
    # path('news/add-news/', add_news, name='add_news'), # Подключаем Добавить новость на главной странице
    path('news/add-news/', CreateNews.as_view() , name='add_news'),  # Подключаем Добавить новость на главной странице
]