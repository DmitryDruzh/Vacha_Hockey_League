from django.urls import path
from .views import *

urlpatterns = [
    path('', AllPlayers.as_view(), name='all_players'),
    path('<slug:player>', InfoOfPlayer.as_view(), name='info_of_player')
]