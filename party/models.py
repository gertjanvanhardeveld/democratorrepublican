from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    """User with app settings."""
    #... your custom fields here
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

    def __unicode__(self):

        return self.user


class Party(models.Model):
    party_name = models.CharField(max_length=255)

    def __unicode__(self):
        return.self.party_name

class Person
    user = foreignkey(customuser)
    party = fk(party)
LOOK AT POLLS & CHOICES
