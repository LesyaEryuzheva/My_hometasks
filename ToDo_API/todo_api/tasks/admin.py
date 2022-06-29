from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'date',
        'status',
    )
    list_editable = ('status',)


admin.site.register(Task, TaskAdmin)
