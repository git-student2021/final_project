from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)   # все поля обязательны к заполнению если blank=True то запишется пустая строка
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d') # upload_to='photos/%Y/%m/%d' django cоздаст папку и будет хранить изображния
    is_publishished = models.BooleanField(default=True)