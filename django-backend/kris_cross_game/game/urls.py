from django.urls import path, include
from .models import Players
from django.views.generic import ListView, DetailView

urlpatterns = [
    path(
        '',
        ListView.as_view(queryset=Players.objects.all().order_by("name"), template_name="html/game.html")
    ),
]