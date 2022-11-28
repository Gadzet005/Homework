from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    fields = ('user', 'text')
    readonly_fields = ('user', 'text')
