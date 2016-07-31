from __future__ import unicode_literals
from django.db import models

class ShortUrl (models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(null=True)
