"""Django admin configuration for the backend app.

Registers the `Tasks` model and exposes sensible list, search,
and filter options for CRUD in the admin interface.
"""

from django.contrib import admin

from backend.models.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """Admin options for the `Tasks` model."""

    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("title", "description")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
