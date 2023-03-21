# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:48:18 2023

@author: bullz
"""

import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shop4Pets.settings')
import django
django.setup()

from pets.models import Pet

fake = Faker()

def add_pet(pet_type):
    name = fake.name()
    age = random.randint(1, 20)
    description = fake.text()
    # You can add a random image or a default image to 'image' field

    pet = Pet.objects.create(
        name=name,
        pet_type=pet_type,
        age=age,
        description=description,
        # image=image,
    )
    return pet

def populate_pets(n=10):
    for _ in range(n):
        pet_type = random.choice(list(Pet.PET_TYPE_CHOICES))
        add_pet(pet_type[0])

if __name__ == '__main__':
    print('Populating database...')
    populate_pets()
    print('Database populated.')
