from django.shortcuts import render
from catalogue.models import Game
# Create your views here.


def home(request):
    all_games = Game.objects.all()
    return render(request, 'home/index.template.html', {
        'all_games':all_games
    })
    