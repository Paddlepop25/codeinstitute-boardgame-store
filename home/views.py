from django.shortcuts import render
from catalogue.models import Game
# Create your views here.

def home(request):
    dixit_game = Game.objects.get(name='Dixit')
    resistance_game = Game.objects.get(name='The Resistance')
    betrayal_game = Game.objects.get(name='Betrayal at House')
    return render(request, 'home/index.template.html', {
        'dixit':dixit_game,
        'resistance':resistance_game,
        'betrayal':betrayal_game
    })
