from django.db import models
from .choices import FILMMAKER_TYPE_CHOICES, GENDER_TYPE_CHOICES

class Planet(models.Model): 
    name = models.CharField(max_length=150, verbose_name='Nombre del planeta')
    population = models.BigIntegerField(blank=True, null=True, verbose_name='Población mundial')

    class Meta:
        verbose_name = "Planeta"
        verbose_name_plural = "Planetas"

    def __str__(self):
        return self.name


class Filmmaking(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=200, verbose_name='Apellidos')
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento')
    type_of_filmmaker = models.IntegerField(choices=FILMMAKER_TYPE_CHOICES, blank=False, null=False,default=0, verbose_name='Director / Productor')

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self):
        return '%s %s - %s ' % (self.first_name, self.last_name, self.type_of_filmmaker) 

class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título de la película')
    description = models.TextField(verbose_name='Sinópsis')
    published_at = models.DateField(verbose_name='Fecha de publicación')
    planets = models.ManyToManyField(Planet, verbose_name='Planetas')
    filmmakers = models.ManyToManyField(Filmmaking, verbose_name='Equipos')

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return '(%s) - %s' % (self.published_at, self.title)

class Character(models.Model): 
    first_name = models.CharField(max_length=150, verbose_name='Nombre')
    last_name = models.CharField(max_length=200, verbose_name='Apellidos')
    date_of_birth = models.CharField(max_length=50, verbose_name='Fecha de nacimiento')
    species = models.CharField(max_length=150, default='N/A', verbose_name='Especie')
    gender = models.CharField(max_length=5,choices=GENDER_TYPE_CHOICES, blank=False, null=False,default='m', verbose_name='Género / Sexo')
    movies = models.ManyToManyField(Movie, verbose_name="Películas")

    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)




