from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Players
# Create your views here.

class AllPlayers(ListView):
    model = Players
    template_name = 'players/all_players.html'
    context_object_name = 'players'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllPlayers, self).get_context_data(**kwargs)
        context['title'] = 'Все игроки'
        return context

class InfoOfPlayer(DetailView):
    model = Players
    template_name = 'players/info_of_player.html'
    context_object_name = 'player'
    slug_url_kwarg = 'player'