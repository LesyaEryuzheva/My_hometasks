from django.contrib import admin
from .models import Category, Clothing


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ClothingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'stock',
        'available',
        'created',
        'updated',
    )
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'stock', 'available')
    search_fields = ['name']


admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Category, CategoryAdmin)
