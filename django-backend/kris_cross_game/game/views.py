from django.shortcuts import render
from .models import Players
from django.http import JsonResponse
from .logic import classes


def game(req):
    fieldXO = classes.FieldXO()
    game_id = req.COOKIES.get('game_id')
    players = Players.objects.order_by("name")
    player = req.POST.get('username')
    coords = req.POST.get("coords")
    context = {
        "list_players": players,
        "player1": player,
        "game_id": game_id,
        'field': fieldXO.get_field(),
        "coords": coords,
    }
    return render(req, 'html/game.html', context)


def create_game(req):
    game_id = req.COOKIES.get('game_id')
    return JsonResponse({'game_id': game_id})
