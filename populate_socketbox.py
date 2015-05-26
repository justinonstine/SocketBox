__author__ = 'justinonstine'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketbox_project.settings')

import django
django.setup()

from socketbox.models import Category, Tool, UserProfile, Location

def populate():


def add_profile(user, address, phoneNumber):
    p = UserProfile.objects.get_or_create(user=user, address=address, phoneNumber=phoneNumber)[0]
    return p

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_location(name, address, city, state):
    l = Location.objects.get_or_create(name=name, address=address, city=city, state=state)[0]
    return l