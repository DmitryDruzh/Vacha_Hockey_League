from django.db import models
from django.urls import reverse
from datetime import date
from clubs.models import Clubs


class Players(models.Model):

    left = 'левый'
    right = 'правый'
    GRIPS = [(left, 'левый'),
             (right, 'правый')]

    DEF = 'защитник'
    ATT = 'нападающий'
    GOA = 'вратарь'
    POSITIONS = [(DEF, 'защитник'),
                 (ATT, 'нападающий'),
                 (GOA, 'вратарь')]

    name = models.CharField(max_length=40, verbose_name='Имя')
    birthday = models.DateField()
    game_number = models.PositiveSmallIntegerField()
    grip = models.CharField(max_length=6, choices=GRIPS)
    club = models.ForeignKey(Clubs, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=40)
    icon = models.ImageField(upload_to='players/%Y/%m/%d')
    position = models.CharField(max_length=15, choices=POSITIONS)
    games = models.PositiveSmallIntegerField(default=0)
    goals = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def get_absolute_url(self):
        return reverse('info_of_player', args=(self.slug,))

    def __str__(self):
        return self.name

    def age(self):
        today = date.today()
        years = today.year - self.birthday.year
        if all((x >= y) for x, y in zip(today.timetuple(), self.birthday.timetuple())):
            return years
        else:
            return years - 1

    def points(self):
        return self.goals + self.assists