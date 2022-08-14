import math

from django.db import models

from math import pi

# Create your models here.

"""
Planets models will consist the name of the planet.
Net circumference and acceleration due to gravity
notice These are required and mass ,diameter,and distance are not required
I  have override the save method to calculate the mass,diameter and distance then save those empty field.
You can put values but it will be overridden  by the save method. 

#To-Do
Second part of the questions require to add exoplanets 
will add a boolean filed of yes or no.
Found the distance using period years
This use keppler's law using luminosity and period years it takes to rotate around the sun
"""


class Planets(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    circumference = models.FloatField(max_length=100, null=True)
    acceleration = models.FloatField(max_length=100, null=True)
    mass = models.CharField(max_length=200, null=True, blank=True)
    diameter = models.CharField(max_length=200, null=True, blank=True)
    distance = models.CharField(null=True, blank=True,max_length=100)
    photo = models.ImageField(null=True, default='default.png')
    period = models.FloatField(null=False, blank=False)
    exo_planet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s mass is:{self.mass}"

    def save(self, *args, **kwargs):
        period_years = self.period
        distance = (period_years ** 2)
        cubic_root = distance**(1/3)
        final_distance = math.floor(cubic_root)
        self.distance = ("Distance{:.1f}AU".format(final_distance))
        print(cubic_root)
        G = 6.67428 * (10 ** -11)
        circumference = self.circumference
        acceleration = self.acceleration
        radius = (circumference) * 1000 / (2 * pi)
        diameter = self.diameter
        diameter = (radius * 2) / 1000
        self.diameter = ("Diameter{:.1f}km".format(diameter))
        mass = (acceleration * radius ** 2) / G
        self.mass = ("{:.1f}(10^21 kg)".format(mass / 10 ** 21))
        super().save(*args, **kwargs)


"""
I created models for the star so i can compare if it is a exoplanet or not , this may be not right 
but  i will set a minimum size for the star so if its less than that size it will be not considered a planet 
Hope this makes sense
"""


class Stars(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    circumference = models.FloatField(max_length=100, null=True)
    acceleration = models.FloatField(max_length=100, null=True)
    mass = models.CharField(max_length=200, null=True, blank=True)
    diameter = models.CharField(max_length=200, null=True, blank=True)
    distance = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(null=True, default='default.png')

    def __str__(self):
        return f"{self.name}'s mass is:{self.mass}"

    def save(self, *args, **kwargs):
        G = 6.67428 * (10 ** -11)
        circumference = self.circumference
        acceleration = self.acceleration
        radius = (circumference) * 1000 / (2 * pi)
        diameter = self.diameter
        diameter = (radius * 2) / 1000
        self.diameter = ("Diameter {:.1f}km".format(diameter))
        mass = (acceleration * radius ** 2) / G
        self.mass = ("{:.1f}(10^21 kg)".format(mass / 10 ** 21))
        super().save(*args, **kwargs)


""" This models will have Many to many relationship with the stars and planets models
cause you can have many stars and planets in a solar system. 
"""


class SolarSystem(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    planets = models.ManyToManyField(Planets)
    stars = models.ManyToManyField(Stars)
    mass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        G = 6.67428 * (10 ** -11)
        super().save(*args, **kwargs)
