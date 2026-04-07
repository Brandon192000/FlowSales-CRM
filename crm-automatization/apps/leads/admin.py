from django.contrib import admin

from apps.leads.infrastructure.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "company",
        "status",
        "source",
        "assigned_to",
        "is_active",
        "created_at",
    )
    list_filter = ("status", "source", "is_active", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "company")
    ordering = ("-created_at",)