from django.urls import path, include
from . import views

urlpatterns = [
    path('main', views.game, name="game"),
    path('create_game', views.create_game, name="create_game"),
]