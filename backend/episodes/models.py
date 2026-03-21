from django.db import models
from characters.models import Character

class Episode(models.Model):
    title = models.CharField(max_length=100)
    air_date = models.DateField()
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title

# Create your models here.
