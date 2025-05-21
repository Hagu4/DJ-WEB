from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название товара")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    added_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата добавления")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'added_date', 'author')
    list_filter = ('added_date', 'author')
    search_fields = ('title', 'short_description')

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.author} на {self.product.title}'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'date')
    list_filter = ('date', 'rating')
    search_fields = ('text', 'author__username')