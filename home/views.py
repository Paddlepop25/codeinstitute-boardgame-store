from django.shortcuts import render
from catalogue.models import Game
# Create your views here.

def home(request):
    try:
        dixit_game = Game.objects.get(name='Dixit')
    except Game.DoesNotExist:
        dixit_game = None
    try:
        resistance_game = Game.objects.get(name='The Resistance')
    except Game.DoesNotExist:
        resistance_game = None
    try:
        catan_game = Game.objects.get(name='Catan')
    except Game.DoesNotExist:
        catan_game = None
    try:
        betrayal_game = Game.objects.get(name='Betrayal at House')
    except Game.DoesNotExist:
        betrayal_game = None
    return render(request, 'home/index.template.html', {
        'dixit':dixit_game,
        'resistance':resistance_game,
        'betrayal':betrayal_game,
        'catan':catan_game
    })
