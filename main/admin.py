from django.contrib import admin
from .models import Planets, SolarSystem, Stars

# Register your models here.
admin.site.register(Planets)
admin.site.register(SolarSystem)
admin.site.register(Stars)
