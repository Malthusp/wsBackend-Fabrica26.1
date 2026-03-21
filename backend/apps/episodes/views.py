from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Episode
from .serializers import EpisodeSerializer
from .services import get_episodes


def episode_list(request):
    data = get_episodes()
    return render(request, 'episodes.html', {'episodes': data})


class EpisodeViewSet(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

# Create your views here.
