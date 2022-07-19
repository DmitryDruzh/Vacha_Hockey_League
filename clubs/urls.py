from django.urls import path
from .views import *

urlpatterns = [
    path('', AllClubs.as_view(), name='all_clubs'),
    path('<slug:club>', InfoOfClub.as_view(), name='info_of_club')
]