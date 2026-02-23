from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """Admin interface for Tasks model."""
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
