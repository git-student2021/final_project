from django import forms
from .models import Category

class NewsForm(forms.Form):
    """Подключаем Добавить новость на главной странице создаем форму"""
    title = forms.CharField(max_length=150)
    content = forms.CharField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
