# Generated by Django 3.0.2 on 2020-07-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200726_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Personaje', 'verbose_name_plural': 'Personajes'},
        ),
        migrations.AlterModelOptions(
            name='filmmaking',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Película', 'verbose_name_plural': 'Películas'},
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'verbose_name': 'Planeta', 'verbose_name_plural': 'Planetas'},
        ),
        migrations.AlterField(
            model_name='character',
            name='movies',
            field=models.ManyToManyField(to='api.Movie', verbose_name='Películas'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='filmmakers',
            field=models.ManyToManyField(to='api.Filmmaking', verbose_name='Equipos'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='planets',
            field=models.ManyToManyField(to='api.Planet', verbose_name='Planetas'),
        ),
    ]
