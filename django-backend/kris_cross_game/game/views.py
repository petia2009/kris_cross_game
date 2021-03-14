from django.shortcuts import render
from .models import Players
from django.http import JsonResponse


def game(req):
    game_id = req.COOKIES.get('game_id')
    players = Players.objects.order_by("name")
    player = req.POST.get('username')
    context = {
        "list_players": players,
        "player1": player,
        "game_id": game_id,
    }
    return render(req, 'html/game.html', context)


def create_game(req):

    return JsonResponse({'qwe': 'rty'})
