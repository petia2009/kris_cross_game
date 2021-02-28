from django.shortcuts import render


def game(req):
    return render(req, 'html/game.html')
