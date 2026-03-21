"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.characters.views import home, character_list, created_characters_list, CharacterViewSet, create_character, delete_character, edit_character
from apps.episodes.views import episode_list
from rest_framework.routers import DefaultRouter
from apps.episodes.views import EpisodeViewSet

router = DefaultRouter()
router.register(r'characters-api', CharacterViewSet)
router.register(r'episodes-api', EpisodeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('characters/', character_list, name='characters'),
    path('characters-create/', create_character, name='characters_create'),
    path('characters-created/', created_characters_list, name='characters_created'),
    path('characters-delete/<int:id>/', delete_character, name='delete_character'),
    path('characters-edit/<int:id>/', edit_character, name='edit_character'),
    path('episodes/', episode_list, name='episodes'),
] + router.urls
