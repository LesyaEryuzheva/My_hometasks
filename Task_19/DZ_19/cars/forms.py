from django import forms
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class BrandForm(forms.Form):
    name = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)


class CarModelForm(forms.Form):
    name_model = forms.CharField(max_length=20)
    car_body = forms.CharField(max_length=20, required=False)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())


class EngineForm(forms.Form):
    type = forms.CharField(max_length=20)
    volume = forms.FloatField()
    car_model = forms.ModelMultipleChoiceField(queryset=CarModel.objects.all(), widget=forms.CheckboxSelectMultiple())
