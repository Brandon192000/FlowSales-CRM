from django.contrib import admin

from apps.contacts.infrastructure.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"first_name",
		"last_name",
		"email",
		"phone",
		"contact_type",
		"company",
		"position",
		"is_active",
		"created_at",
	)
	list_filter = ("contact_type", "is_active", "created_at")
	search_fields = ("first_name", "last_name", "email", "phone", "company")
	ordering = ("-created_at",)
