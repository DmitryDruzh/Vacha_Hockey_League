from django.urls import path
from .views import *

urlpatterns = [
    path('', all_news, name='all_news'),
]