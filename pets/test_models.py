# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:55:21 2023

@author: bullz
"""

from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def test_homepage_returns_200(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


from pets.models import Category, Page

class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Cats')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Cats')
        self.assertEqual(self.category.slug, 'cats')

class PageModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dogs')
        self.page = Page.objects.create(category=self.category, title='Poodle', pet_name='Rufus', age=5, breed='Poodle', contact='example@example.com', description='A cute poodle', image='poodle.jpg')

    def test_page_str_method(self):
        self.assertEqual(str(self.page), 'Poodle')
