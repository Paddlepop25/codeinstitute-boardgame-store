from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Game, Category
from .forms import GameForm, GameSearchForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

def show_games(request):
    all_games = Game.objects.all()
    party_games = all_games.filter(category_id=1).order_by('name')
    card_games = all_games.filter(category_id=2).order_by('name')
    board_games = all_games.filter(category_id=3).order_by('name')
    filtering = True
    results = True
    search_terms = request.GET.get('search_terms')
    
    if search_terms == None:
          filtering = False
      
    else:
        all_games = all_games.filter(Q(name__icontains=search_terms) | Q(category__name__icontains=search_terms) | Q(description__icontains=search_terms))
     
    if all_games.exists():
        pass
        
    else:
        all_games = None
        results = False
        
    return render(request, 'catalogue/games.template.html', {
        'all_games':all_games,
        'search_terms':search_terms,
        'party_games':party_games,
        'card_games':card_games,
        'board_games':board_games,
        'filtering':filtering,
        'results':results
    })

# function works only for superusers
@user_passes_test(lambda u: u.is_superuser)
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

# function works only for superusers
@user_passes_test(lambda u: u.is_superuser)
def update_game(request, game_id):
    game_being_updated = get_object_or_404(Game, pk=game_id)
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    
    if request.method == "POST":
        # for updating form
        update_game_form = GameForm(request.POST, instance=game_being_updated)
        if update_game_form.is_valid():
            update_game_form.save()
            messages.success(request, "Game has been updated successfully")
            return redirect(reverse(show_games))
    else:
        update_game_form = GameForm(instance=game_being_updated)

    return render(request, 'catalogue/update_game.template.html',{
        'form':update_game_form,
        'game':game_being_deleted
    })    

@user_passes_test(lambda u: u.is_superuser)
def confirm_delete_game(request, game_id):
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    return render(request, 'catalogue/confirm_delete_game.template.html', {
        'game':game_being_deleted
    })    

@user_passes_test(lambda u: u.is_superuser)
def actually_delete_game(request, game_id):
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    game_being_deleted.delete()
    messages.success(request, "Game has been deleted successfully")
    return redirect(reverse('show_games'))     

def game_info(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'catalogue/game_info.template.html', {
        'game':game
    })    