from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_publishished')
    # поля которые видно в админке
    list_display_links = ('id', 'title') #поля которые должны быть ссылками
    search_fields = ('title', 'content') # поля по которым производится поиск
    list_editable = ('is_publishished',)# можно добавлять , появляются чек-боксы
    list_filter = ('is_publishished', 'category') # можно сортировать по полям


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # поля которые видно в админке
    list_display_links = ('id', 'title') #поля которые должны быть ссылками
    search_fields = ('title',) # поля по которым производится поиск


admin.site.register(News, NewsAdmin) #регистрация моделей в админке  !Порядок важен
admin.site.register(Category, CategoryAdmin)
