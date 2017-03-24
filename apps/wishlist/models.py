from __future__ import unicode_literals

from django.db import models

from ..logreg.models import User

class Item(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    User = models.ForeignKey(User, related_name = 'items')

class Wishlist(models.Model):
    User = models.ForeignKey(User, related_name = 'wish_users')
    Item = models.ForeignKey(Item, related_name = 'wish_items')

# Create your models here.
