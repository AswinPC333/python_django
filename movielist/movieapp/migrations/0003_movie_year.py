# Generated by Django 4.2.10 on 2024-02-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default='2023'),
            preserve_default=False,
        ),
    ]
