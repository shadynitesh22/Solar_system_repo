# Generated by Django 4.1 on 2022-08-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_planets_photo_stars_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='planets',
            name='exo_planet',
            field=models.BooleanField(default=False),
        ),
    ]
