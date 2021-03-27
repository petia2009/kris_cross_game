from django.shortcuts import render
from django.http import JsonResponse
from .logic import classes

GAMES = {}


def game(req):
    game_id_cookie = req.COOKIES.get("game_id")
    is_new_game = req.POST.get("new_game")
    player = req.POST.get('username')
    coords = req.POST.get("coords")

    context = {
        'player1': player
    }

    if is_new_game:
        game = classes.Game()
        GAMES[game.get_game_id()] = game
        field_xo = game.get_field_class()
        whoose_move = field_xo.get_whoose_move()
        context['field'] = field_xo.get_field()
        context['winner'] = None
    else:
        game = GAMES.get(game_id_cookie)
        field_xo = game.get_field_class()
        whoose_move = field_xo.get_whoose_move()
        context['field'] = field_xo.get_field()
        context['winner'] = None

    if coords:
        coords = coords.split(" ")
        coords = list(map(lambda a: int(a), coords))
        if field_xo.is_this_move_win(whoose_move, coords[1], coords[0]):
            context['winner'] = whoose_move

    response = render(req, 'html/game.html', context)
    response.set_cookie('game_id', game.get_game_id())

    return response


def create_game(req):
    game_id = req.COOKIES.get('game_id')
    return JsonResponse({'game_id': game_id})
