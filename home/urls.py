from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
