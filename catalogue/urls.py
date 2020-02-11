from django.urls import path
from .views import show_games, create_game, update_game, confirm_delete_game, actually_delete_game, game_info  # .views in this same directory

urlpatterns = [
    path('', show_games, name='show_games'),
    path('create', create_game, name='create_game'),
    path('update/<game_id>', update_game, name='update_game'),
    path('confirm_delete/<game_id>', confirm_delete_game, name='confirm_delete'),
    path('actually_delete/<game_id>', actually_delete_game, name='delete_game'),
    path('game_info/<game_id>', game_info, name='game_info'),
]