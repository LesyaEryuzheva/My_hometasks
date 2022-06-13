from django.shortcuts import render

from .forms import BrandForm, CarModelForm, EngineForm
from .models import Brand, CarModel, Engine


def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            Brand.objects.create(
                name=form.cleaned_data['name'],
                country=form.cleaned_data['country']
            )
    form = BrandForm()
    context = {'form': form}
    return render(request, 'cars/catalog.html', context)


def create_car_model(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            CarModel.objects.create(
                name_model=form.cleaned_data['name_model'],
                car_body=form.cleaned_data['car_body'],
                brand=form.cleaned_data['brand'],
            )
    form = CarModelForm()
    context = {'form': form}
    return render(request, 'cars/car_model.html', context)


def create_engine(request):
    if request.method == 'POST':
        form = EngineForm(request.POST)
        if form.is_valid():
            engine = Engine.objects.create(
                         type=form.cleaned_data['type'],
                         volume=form.cleaned_data['volume']
                     )
            car_models = form.cleaned_data['car_model']
            for car_model in car_models:
                engine.car_model.add(car_model)
    form = EngineForm()
    context = {'form': form}
    return render(request, 'cars/engine.html', context)
