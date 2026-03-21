from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length=200)
    episode_code = models.CharField(max_length=20, null=True, blank=True)
    air_date = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Create your models here.
