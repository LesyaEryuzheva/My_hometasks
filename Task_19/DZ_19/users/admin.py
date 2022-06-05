from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, PersonalInfo


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_superuser', 'groups'),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    list_filter = ('is_superuser', 'is_active')
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_superuser',
        'is_active',
    )
    ordering = ('email',)
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(User, CustomUserAdmin)
admin.site.register(PersonalInfo)
