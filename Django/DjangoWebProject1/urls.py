"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from app.views import catalog, product_detail
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static

 



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('catalog/', catalog, name='catalog'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('repair/', views.repair, name='repair'),  
    path('news/', views.news, name='news'),  
    path('useful-resources/', views.useful_resources, name='useful_resources'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('newproduct/', views.newproduct, name='newproduct'),
    path('video/', views.videopost, name='video'),
    path('login/',
          LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
