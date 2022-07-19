from django.db import models
from django.urls import reverse

# Create your models here.

class Clubs(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    icon = models.ImageField(upload_to='clubs/&Y/&m/&d')
    slug = models.SlugField(default='', null=False)

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info_of_club', args=(self.slug,))