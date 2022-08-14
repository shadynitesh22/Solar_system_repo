from django import forms
from django.forms import ModelForm
from .models import Planets, SolarSystem, Stars


class SolarSystemForm(ModelForm):
    class Meta:
        model = SolarSystem
        exclude = ['mass', 'diameter', 'acceleration', 'circumference']
        widgets = {
            'planets': forms.CheckboxSelectMultiple(),
            'stars': forms.CheckboxSelectMultiple()
        }


class PlanetsForm(ModelForm):
    class Meta:
        model = Planets
        exclude = ['mass', 'diameter', 'distance', 'exo_planet']


class StarsForm(ModelForm):
    class Meta:
        models = Stars
        exclude = ['mass', 'diameter', 'distance']
