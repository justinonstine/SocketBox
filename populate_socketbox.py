__author__ = 'justinonstine'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketbox_project.settings')

import django
django.setup()

from socketbox.models import Category, Tool, UserProfile, Location
from django.contrib.auth.models import User

def populate():
    justin = get_user("oaf")
    erin = get_user("erin")

    justinProfile = add_profile(justin, "1047 Ruby St", "4156804727")
    erinProfile = add_profile(erin, "1047 Ruby St", "4156804727")


def get_user(username):
    u = User.objects.get(username=username)
    return u

def add_profile(user, address, phoneNumber):
    p = UserProfile.objects.get_or_create(user=user, address=address, phoneNumber=phoneNumber)[0]
    return p

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_location(name, address, city, state):
    l = Location.objects.get_or_create(name=name, address=address, city=city, state=state)[0]
    return l

def add_tool(name, description, permanentLocation, owner, category=None, lastLoaned=None,
             dueDate=None, set=None, size=None, unitType=None, accessory=None):
    t = Tool.objects.get_or_create(name=name, size=size, unitType=unitType,
                                   description=description, permanentLocation=permanentLocation,
                                   currentLocation=permanentLocation, caretaker=owner)[0]
    if t:
        t.owners.add(owner)
        if category:
            t.category.add(category)
        if lastLoaned:
            t.lastLoaned = lastLoaned
        if dueDate:
            t.dueDate = dueDate
        if accessory:
            t.accessory.add(accessory)
        if set:
            t.set = set
    return t