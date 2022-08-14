from django.urls import path

from .views import show_home, create_planets, create_solar_system, discover_planets, find_weight

urlpatterns = [
    path("", show_home, name='home-page'),
    path("create-solar-system/", create_solar_system, name='solar-system'),
    path("planets/", create_planets, name='planets'),
    path("discover/", discover_planets, name="discover"),
    path("weight/<str:pk>/", find_weight, name="find_weight")

]
