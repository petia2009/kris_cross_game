from django.shortcuts import render
from .models import Players


def game(req):
    players = Players.objects.order_by("name")
    player = req.POST.get('username')
    context = {
        "list_players": players,
        "player1": player
    }
    return render(req, 'html/game.html', context)
