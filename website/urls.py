# criar arquivo urls.py dentro da pasta website
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('missao/', views.missao, name='missao'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact')

]
