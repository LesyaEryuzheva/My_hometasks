from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'date',
        'description',
    )


admin.site.register(Todo, TodoAdmin)
