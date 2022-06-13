from django.contrib import admin

from .models import Engine, CarModel


class EngineInLine(admin.TabularInline):
    model = Engine.car_model.through

    def has_delete_permission(self, request, obj=None):
        return False


class CarModelInLine(admin.StackedInline):
    model = CarModel
