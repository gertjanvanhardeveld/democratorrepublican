from django.db import models
from django.contrib.auth.models import User, UserManager

class Party(models.Model):
    party = models.CharField(max_length=200)
    party_slug = models.SlugField()
    def __unicode__(self):
        return self.party

class City(models.Model):
    city = models.CharField(max_length=200)
    city_slug = models.SlugField()
    def __unicode__(self):
        return self.city

class State(models.Model):
    state = models.CharField(max_length=200)
    state_slug = models.SlugField()
    def __unicode__(self):
        return self.state

class CustomUser(User):
    """User with app settings."""
    party = models.ForeignKey(Party)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    zipcode = models.CharField(max_length=5)
    message = models.TextField()
    objects = UserManager()

    def __unicode__(self):

        return self.user
