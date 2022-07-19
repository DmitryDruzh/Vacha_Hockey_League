from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Clubs


# Create your views here.

class AllClubs(ListView):
    model = Clubs
    template_name = 'clubs/all_clubs.html'
    context_object_name = 'clubs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все клубы'
        return context

    # def get_queryset(self):
    #     return Clubs.objects.get(slug=self.kwargs['slug'])


class InfoOfClub(DetailView):
    model = Clubs
    template_name = 'clubs/info_of_club.html'
    context_object_name = 'club'
    slug_url_kwarg = 'club'