from django.shortcuts import render
from .models import Episode
from .services import get_episodes

def episode_list(request):
    data = get_episodes()
    return render(request, 'episodes.html', {'episodes': data})

# Create your views here.
