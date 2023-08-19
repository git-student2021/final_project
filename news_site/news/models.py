from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')   # все поля обязательны к заполнению если blank=True то запишется пустая строка
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обнавлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True) # upload_to='photos/%Y/%m/%d' django cоздаст папку и будет хранить изображния
    is_publishished = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'      #наименование модели в единственнои числе
        verbose_name_plural = 'Новости'   #наименование модели во множественном числе
        ordering = ['-created_at'] # сортировать по убыванию свежая новость сверху


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование  катенории')

    class Meta:
        verbose_name = 'Категория'      #наименование модели в единственнои числе
        verbose_name_plural = 'Категории'   #наименование модели во множественном числе
        ordering = ['title'] # сортировать по названию

