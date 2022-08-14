# Generated by Django 4.1 on 2022-08-12 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('circumference', models.FloatField(max_length=100, null=True)),
                ('acceleration', models.FloatField(max_length=100, null=True)),
                ('mass', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolarSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('planets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.planets')),
            ],
        ),
    ]
