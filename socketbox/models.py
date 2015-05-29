from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    """
    A physical location where a tool might reside
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)


class Category(models.Model):
    """
    A Category of tools. Something like, "saw" or "hammer" or "wrench" where
    it defines a group of potential matches like a hacksaw or a socket wrench
    """
    name = models.CharField(max_length=30)


class Set(models.Model):
    """
    Represents a set of tools, like a wrench set with various sizes. Mostly
    for convenience.
    """
    name = models.CharField(max_length=30)


class Community(models.Model):
    """
    A group of friends/people who share tools amongst themselves
    """
    name = models.CharField(max_length=50)


class UserProfile(models.Model):
    """
    UserProfile
    This just stores a little extra information about a user than what the
    standard Django user model provides
    """
    address = models.ForeignKey(Location, related_name="home_address")
    phoneNumber = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    communities = models.ManyToManyField(Community)
    locations = models.ManyToManyField(Location)


class Tool(models.Model):
    """
    This is the base model for an individual tool
    """
    METRIC = 'ME'
    IMPERIAL = 'IM'
    UNIT_CHOICES = (
        (METRIC, 'Metric'),
        (IMPERIAL, 'Imperial')
    )
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=30, blank=True)
    unitType = models.CharField(max_length=2,
                                choices=UNIT_CHOICES,
                                default=IMPERIAL, blank=True)
    description = models.CharField(max_length=500, blank=True)
    permanentLocation = models.ForeignKey(Location, related_name="permanent_location")
    currentLocation = models.ForeignKey(Location, related_name="current_location")
    owners = models.ManyToManyField(UserProfile)
    caretaker = models.ForeignKey(UserProfile, related_name="caretaker")
    category = models.ManyToManyField(Category)
    lastLoaned = models.DateField(null=True)
    dueDate = models.DateField(null=True)
    set = models.ForeignKey(Set, null=True)

    #  A drill is not a bit's accessory, so symmetrical is false
    accessory = models.ManyToManyField("self", symmetrical=False)




