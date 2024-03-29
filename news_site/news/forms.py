from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # UserCreationFormформа создания пользователя, AuthenticationForm авторизация пользователя
from django.contrib.auth.models import User

# class NewsForm(forms.Form):
#     """Подключаем Добавить новость на главной странице создаем форму, форма не связана с моделью"""
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5
#     }))
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True, widget=forms.CheckboxInput())
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    """Создаем поля которые будут видны при регистрации"""
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsForm(forms.ModelForm):
    """форма связана с моделью"""
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        """дополнительная валидация"""
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
