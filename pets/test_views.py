# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:54:46 2023

@author: bullz
"""

from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def test_homepage_returns_200(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


from django.urls import reverse
from pets.models import PetAd

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/home.html')

class AdDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.ad = PetAd.objects.create(pet_name='Cat', description='A fluffy cat', image='cat.jpg', contact_info='example@example.com')

    def test_ad_detail_view(self):
        response = self.client.get(reverse('ad_detail', args=[self.ad.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/ad_detail.html')
