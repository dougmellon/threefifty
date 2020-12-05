from django.db import models
from django.urls import reverse

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=500, null=True)
    comic = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    food = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse('hero_detail', args=[str(self.id)])
