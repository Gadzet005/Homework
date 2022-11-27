from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ('date_joined', 'is_active', 'last_login')
    list_display = (
        'username', 'email', 'birthday_date', 'is_staff', 'is_superuser'
        )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Персональная информация', {
                'fields': (
                    'username', 'birthday_date'
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
