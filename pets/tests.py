# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:55:31 2023

@author: bullz
"""

from django.test import TestCase
from django.urls import reverse
from pets.models import PetAd


class PetAdModelTests(TestCase):
    def test_str_representation(self):
        pet_ad = PetAd(pet_name='Test Pet')
        self.assertEqual(str(pet_ad), 'Test Pet')

class PetAdViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Shop 4 Pets')
