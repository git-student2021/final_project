from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    # поля которые видно в админке
    list_display_links = ('id', 'title') #поля которые должны быть ссылками
    search_fields = ('title', 'content') # поля по которым производится поиск
    list_editable = ('is_published',)# можно добавлять , появляются чек-боксы
    list_filter = ('is_published', 'category') # можно сортировать по полям
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    # поля которые видно в самой новости
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at') #поля только для чтения
    save_on_top = True # добавляет поля сверху (для сохранения, удалить и т.д.)

    def get_photo(self, obj):  #проедстовление фото в виде html  кода
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # поля которые видно в админке
    list_display_links = ('id', 'title') #поля которые должны быть ссылками
    search_fields = ('title',) # поля по которым производится поиск


admin.site.register(News, NewsAdmin) #регистрация моделей в админке  !Порядок важен
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'