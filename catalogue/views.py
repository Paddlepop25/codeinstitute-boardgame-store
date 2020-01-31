from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Game
from .forms import GameForm

# Create your views here.
def show_games(request):
    all_games = Game.objects.all()
    return render(request, 'catalogue/games.template.html', {
        'all_games':all_games
    })
    
def create_game(request):
    if request.method == 'POST':
        create_game_form = GameForm(request.POST)
        if create_game_form.is_valid():
            create_game_form.save()
            return redirect(reverse(show_games))

    else:
        create_game_form = GameForm()

    return render(request, 'catalogue/create_game.template.html', {
        'form':create_game_form
    })    

def update_game(request, game_id):
    game_being_updated = get_object_or_404(Game, pk=game_id)

    if request.method == "POST":
        # for update
        update_game_form = GameForm(request.POST, instance=game_being_updated)
        if update_game_form.is_valid():
            update_game_form.save()

            # always make sure to return the redirect
            return redirect(reverse(show_games))
    else:
        update_game_form = GameForm(instance=game_being_updated)

    return render(request, 'catalogue/update_game.template.html',{
        'form':update_game_form
    })    
    
def confirm_delete_game(request, game_id):
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    return render(request, 'catalogue/confirm_delete_game.template.html', {
        'game':game_being_deleted
    })    
    
def actually_delete_game(request, game_id):
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    game_being_deleted.delete()
    return redirect(reverse('show_games'))     