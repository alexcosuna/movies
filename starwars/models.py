from django.db import models

class History(models.Model):
    url = models.URLField()
    date = models.DateTimeField()