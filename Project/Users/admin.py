from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ('date_joined', 'last_login')
    list_display = (
        'nickname', 'email', 'birthday_date', 'is_staff', 'is_superuser'
        )
    ordering = ('nickname',)
    search_fields = ('nickname', 'email')
    list_display_links = ('nickname',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Персональная информация', {
                'fields': (
                    'nickname', 'birthday_date'
                    )
            }
        ),
        (
            'Права и разрешения', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                    )
            }
        ),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2'),
        }),
    )
