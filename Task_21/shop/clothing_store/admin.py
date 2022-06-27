from django.contrib import admin

from .models import Brand, Clothing, Item


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ClothingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'brand',
        'available',
    )
    list_editable = ('price', 'available')
    search_fields = ['name']


admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Item, ItemAdmin)
