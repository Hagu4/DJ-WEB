"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .feedback_forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import BootstrapAuthenticationForm
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product, Review
from .forms import ReviewForm
from django.utils import timezone


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Добро пожаловать на страницу "О нас"!',
            'year':datetime.now().year,
        }
    )

def catalog(request):
    products = Product.objects.all()  # Получите все товары
    return render(request, 'app/catalog.html', {
        'title': 'Каталог',
        'products': products,  # Передайте товары в шаблон
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product).order_by('-date')

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.date = timezone.now()
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'app/product_detail.html', {
        'title':'Подробнее о товаре',
        'product': product,
        'reviews': reviews,
        'form': form
    })

def newproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('catalog')  # Переадресация на страницу каталога
    else:
        form = ProductForm()
    return render(request, 'app/newproduct.html', {'title':'Добавление нового продукта','form': form})  # Убедитесь, что путь указан

def repair(request):
    return render(request, 'app/repair.html',
                  {
                  'title':'Ремонт',
                  }
                )

def videopost(request):
    return render(request, 'app/videopost.html',{'title':'Видео нашей работы'})

def news(request):
    return render(request, 'app/news.html',
                  {
                  'title':'Новости',
                  }
                  )

def useful_resources(request):
   
    resources = [
        {
            'title': 'Официальная документация Bosch',
            'url': 'https://www.bosch-pt.com/',
            'description': 'Сайт Bosch Professional с руководствами и инструкциями для электроинструментов.',
        },
        {
            'title': 'Makita Россия',
            'url': 'https://www.makita.ru/',
            'description': 'Официальный сайт Makita в России. Каталог инструментов и поддержка.',
        },
        {
            'title': 'Husqvarna - Официальный сайт',
            'url': 'https://www.husqvarna.com/',
            'description': 'Сайт Husqvarna с информацией о бензоинструментах и садовой технике.',
        },
        {
            'title': 'Каталог запчастей для инструментов',
            'url': 'https://www.220-volt.ru/',
            'description': 'Сайт с запчастями для электроинструментов и бензоинструментов.',
        },
        {
            'title': 'Советы по выбору инструментов',
            'url': 'https://vyboroved.ru/',
            'description': 'Ресурс с обзорами и рекомендациями по выбору инструментов.',
        },
        ]
    return render(request, 'app/useful_resources.html', {'resources': resources, 'title': 'Полезные ресурсы',})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
           
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'rating': form.cleaned_data['rating'],
                'usability': form.cleaned_data['usability'],
                'frequency': form.cleaned_data['frequency'],
                'comments': form.cleaned_data['comments'],
            }
            return render(request, 'app/feedback_thanks.html', {'data': data,'title':'Спасибо за отзыв',})
    else:
        form = FeedbackForm()

    return render(request, 'app/feedback.html', {'form': form,'title':'Обратная связь',})

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":  
        regform = UserCreationForm(request.POST)
        if regform.is_valid():  
            reg_f = regform.save(commit=False)  
            reg_f.is_staff = False  
            reg_f.is_active = True  
            reg_f.is_superuser = False  
            reg_f.date_joined = datetime.now()  
            reg_f.last_login = datetime.now()  
            reg_f.save()  
            return redirect('login')  
    else:
        regform = UserCreationForm()  
    return render(
        request,
        'app/registration.html',
        {
            'title':'Регистрация',
            'regform': regform,  
            'year': datetime.now().year,
        }
    )

def login_view(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление после успешного входа
    else:
        form = BootstrapAuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

