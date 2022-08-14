import math

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Planets, SolarSystem
from .forms import SolarSystemForm, PlanetsForm, StarsForm

# Create your views here.
"""
This function is displaying the data in the Ui

"""


def show_home(request):
    planets = Planets.objects.all()
    solar_system = SolarSystem.objects.all()
    context = {"planets": planets, "solar_system": solar_system}
    return render(request, "home.html", context)


"""
This function will discover exoplanets and their distance from our solar system.
What is exoplanets : Planets beyond our solar system
How to find the distance between two solar system.

"""
"""
Finding the mass of solar system by totaling the weight of every planets and stars in it.

"""


def find_weight(request, pk):
    adds = 0
    results = []
    final_val = 0
    solar_system = SolarSystem.objects.filter(id=pk)
    for i in solar_system:
        planets = i.planets.all()

        for a in planets:
            size = a.mass
            value = size.split(".")[::-1]
            a, b = value
            val = int(b)
            results.append(val)
        print(results)
        for x in results:
            adds += x

            final_val = ("{:.1f}(10^21 kg)".format(adds))

        return HttpResponse(f"Total Mass of the Solar System:{final_val}")

    context = {"solar_system": solar_system, "solar_system_mass": final_val}
    return render(request, "find-weight.html", context)


# def discover_planets(request):
#     planets = Planets.objects.all()
#     solar = SolarSystem.objects.all()
#     for i in solar:
#         exo = i.planets.all()
#         name = i.planets.name
#         print(name)
#         for _ in planets:
#             if exo != _:
#                 exo = _.exo_planet = True
#                 print(exo)
#                 #
#         #         if e_p:
#         #             ep = False
#         #     else:
#         #         ep = _.exo_planet
#         #         ep = True
#         #         return exo
#     context = {"solar": solar}
#     return render(request, 'solar_system.html', context, planets)


def create_solar_system(request):
    form = SolarSystemForm()
    if request.method == "POST":
        form = SolarSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {"form": form}
    return render(request, "create-solar.html", context)


def create_planets(request):
    form = PlanetsForm()
    if request.method == 'POST':
        form = PlanetsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {"form": form}
    return render(request, 'create-planets.html', context)
