from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    fields = ('email', 'text')
    readonly_fields = ('email', 'text')
