# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:15 2023

@author: bullz
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    
    
    
    ]