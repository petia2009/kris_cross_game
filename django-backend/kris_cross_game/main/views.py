from django.shortcuts import render

# Create your views here.
def main(req):
    response = render(req, 'html/main.html')
    response.set_cookie('game_id', '')
    response.set_cookie('player_token', "")
    return response
