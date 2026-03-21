from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_characters

@api_view(['GET'])
def external_characters(request):
    data = get_characters()
    return Response(data)

# Create your views here.
