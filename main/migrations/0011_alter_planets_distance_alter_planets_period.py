# Generated by Django 4.1 on 2022-08-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_planets_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='period',
            field=models.FloatField(),
        ),
    ]
