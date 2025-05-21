
from django import forms
from .models import Review, Product
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'short_description', 'full_description', 'price', 'image']
        labels = {
            'title': 'Название товара',
            'short_description': 'Краткое описание',
            'full_description': 'Полное описание',
            'price': 'Цена',
            'image': 'Изображение'
        }
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {
            'text': 'Ваш отзыв',
            'rating': 'Рейтинг'
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'rating-input'})
        }
