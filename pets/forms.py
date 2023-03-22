# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:17:59 2023

@author: bullz
"""

from django import forms
from django.contrib.auth.models import User
from pets.models import Category, Page, UserProfile
from django.core.validators import MinValueValidator

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the pet type (e.g., dog, cat, or bird).")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the advert.")
    pet_name = forms.CharField(max_length=100, help_text="Please enter the name of the pet.")
    age = forms.IntegerField(validators=[MinValueValidator(0)], help_text="Please enter the pet's age.")
    breed = forms.CharField(max_length=100, help_text="Please enter the pet's breed.")
    contact = forms.CharField(max_length=255, help_text="Please enter your contact information.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please enter a brief description of the pet.")
    image = forms.ImageField(required=False, help_text="Upload an image of the pet (optional).")

    class Meta:
        model = Page
        exclude = ('category',)
        # or use fields attribute: fields = ('title', 'pet_name', 'age', 'breed', 'contact', 'description', 'image')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
