from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
    )
    filter_horizontal = ('items',)


admin.site.register(Order, OrderAdmin)
