from __future__ import print_function
from __future__ import division
from math import pi

G = 6.67428 * (10 ** -11)

user_circum = float(input("Circumference (km) of planet? "))
user_acc = float(input("Acceleration due to gravity (m/s^2)?"))


def display_results(radius, mass, velocity, distance):
    print("Radius of the planet {:.1f}km".format(radius / 1000))
    print("Mass of the planet {:.1f}(10^21 kg)".format(mass / 10 ** 21))
    print("Escape velocity of the planet {:.1f}(km.s)".format(velocity / 1000))
    print("distance :", distance)


def escape_velocity(circumference, acceleration):
    circumference = float(circumference)
    acceleration = float(acceleration)
    radius = circumference * 1000 / (2 * pi)
    distance = (radius * 2) / 1000
    mass = (acceleration * radius ** 2) / G
    vEscape = ((2 * G * mass) / radius) ** 0.5
    display_results(radius, mass, vEscape, distance)


escape_velocity(user_circum, user_acc)
