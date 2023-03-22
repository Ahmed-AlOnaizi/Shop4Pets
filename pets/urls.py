# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:15 2023

@author: bullz
"""

from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/',views.about, name = "about"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('add_page/<str:category_name_slug>/', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('login/', views.user_login, name='login'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    
    
    
    ]