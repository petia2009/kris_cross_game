from django.shortcuts import render
from .models import Players
from django.http import JsonResponse
from .logic import classes

fieldXO = classes.FieldXO()

def game(req):
    whoose_move = fieldXO.get_whoose_move()
    game_id = req.COOKIES.get('game_id')
    players = Players.objects.order_by("name")
    player = req.POST.get('username')
    coords = req.POST.get("coords")
    if not coords == None:
        coords = coords.split(" ")
        coords = list(map(lambda a: int(a), coords))
        fieldXO.move(whoose_move, coords[1], coords[0])
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
