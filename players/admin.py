from django.contrib import admin
from .models import Players

# Register your models here.

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    fields = ['game_number', 'name', 'birthday', 'club', 'position', 'slug', 'icon', 'games', 'goals', 'assists', 'grip']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'game_number', 'club', 'position', 'games', 'goals', 'assists']
    list_filter = ['position', 'club']