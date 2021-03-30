from django.db import models


class History(models.Model):
    url = models.URLField()
    date = models.DateTimeField()

    def __str__(self):
        return self.url


class PeopleImage(models.Model):
    peoples = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.peoples
