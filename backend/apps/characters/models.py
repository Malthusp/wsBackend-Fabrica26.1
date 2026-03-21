from django.db import models
from apps.users.models import User

class Character(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
