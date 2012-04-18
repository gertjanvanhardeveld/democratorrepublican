from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Party(models.Model):
    party = models.CharField(max_length=200)
    party_slug = models.SlugField()
    def get_absolute_url(self):
        return "/party/%i/" % self.id
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

class CustomUser(models.Model):
    user = models.ForeignKey(User)
    party = models.ForeignKey(Party)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    zipcode = models.CharField(max_length=5)
    message = models.TextField()

    def __unicode__(self):

        return self.user.username

class CustomUserForm(ModelForm):
    class Meta:
        #exclude = ('user',)
        model = CustomUser





