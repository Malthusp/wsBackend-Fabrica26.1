from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save

def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)