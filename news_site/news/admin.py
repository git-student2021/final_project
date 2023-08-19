from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_publishished')
    # поля которые видно в админке
    list_display_links = ('id', 'title') #поля которые должны быть ссылками
    search_fields = ('title', 'content') # поля по которым производится поиск



admin.site.register(News, NewsAdmin) #регистрация моделей в админке  !Порядок важен

