from django.shortcuts import render
from .models import Players


def game(req):
    players = Players.objects.order_by("name")
    context = {
        "list_players": players
    }
    return render(req, 'html/game.html', context)
