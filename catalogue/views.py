from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Game
from .forms import GameForm, GameSearchForm

# Create your views here.
def show_games(request):
    # search_form = GameSearchForm(request.GET)
    all_games = Game.objects.all()
    # field_name = 'price'
    # obj = Game.objects.all()
    # price_strikethrough = getattr(all_games, field_name)
    print(Game)
    # price_strikethrough = all_games.filter(request.GET.get('price'))
    
    # if search_form.data.get('search_terms'):
    #     # like SELECT * FROM courses WHERE title LIKE '%react%'
    #     all_games = all_games.filter(name__contains=search_form.data['search_terms'])

    # if request.GET.get('min_cost'):
    #     all_games = all_games.filter(price__gte=request.GET.get('min_cost'))


    # if request.GET.get('max_cost'):
    #     all_games = all_games.filter(price__lte=request.GET.get('max_cost'))
        
        
    if request.GET.get('search_terms'):
        search_terms = request.GET.get('search_terms')
        all_games = all_games.filter(name__icontains=search_terms)
        # print(list(all_games))
        
    return render(request, 'catalogue/games.template.html', {
        'all_games':all_games,
        # 'price_strikethrough':price_strikethrough
        # 'search_form':search_form
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
    # all_games = Game.objects.all()
    game_being_updated = get_object_or_404(Game, pk=game_id)
    game_being_deleted = get_object_or_404(Game, pk=game_id)
    
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
        'form':update_game_form,
        'game':game_being_deleted
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

def game_info(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'catalogue/game_info.template.html', {
        'game':game
    })    