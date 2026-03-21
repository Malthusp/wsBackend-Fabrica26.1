from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_characters
from rest_framework.viewsets import ModelViewSet
from .models import Character
from .serializers import CharacterSerializer
from django.contrib.auth.decorators import login_required

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

@api_view(['GET'])
def external_characters(request):
    data = get_characters()
    return Response(data)

def home(request):
    return render(request, 'home.html')

def character_list(request):
    data = get_characters()
    return render(request, 'characters.html', {'characters': data})

def created_characters_list(request):
    characters = Character.objects.all()
    return render(request, 'created_characters.html', {'characters': characters})

@login_required
def create_character(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        species = request.POST.get('species')

        Character.objects.create(
            name=name,
            status=status,
            species=species,
            created_by=request.user
        )

        return redirect('characters_created')

    return render(request, 'create_character.html')

@login_required
def delete_character(request, id):
    character = get_object_or_404(Character, id=id)

    # segurança: só quem criou pode deletar
    if character.created_by == request.user:
        character.delete()

    return redirect('characters_created')

# Create your views here.
