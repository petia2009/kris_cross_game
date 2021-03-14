from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def main(req):
    response = render(req, 'html/main.html')
    response.set_cookie('game_id', 'game_id')
    return response
