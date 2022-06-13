from django.contrib import admin

from .models import Brand, CarModel, Engine
from .inlines import EngineInLine, CarModelInLine


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
    )
    inlines = (CarModelInLine,)
    search_fields = ('name', 'country')


class CarModelAdmin(admin.ModelAdmin):
    inlines = (EngineInLine,)
    list_display = (
        'name_model',
        'car_body',
    )
    search_fields = ('name_model', 'car_body')
    ordering = ('name_model',)
    raw_id_fields = ('brand',)


class EngineAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'volume',
    )
    search_fields = ('type', 'volume')
    filter_horizontal = ('car_model',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Engine, EngineAdmin)
