# Generated by Django 4.2.10 on 2024-02-20 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]