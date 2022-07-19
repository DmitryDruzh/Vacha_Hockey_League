from django.contrib import admin
from .models import Clubs

# Register your models here.

@admin.register(Clubs)
class ClubsAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    prepopulated_fields = {'slug': ('name',)}