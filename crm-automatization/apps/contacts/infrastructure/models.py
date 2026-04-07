from django.db import models
from django.core.validators import MinLengthValidator
from apps.contacts.domain.constants import ContactType

class Contact(models.Model):
	first_name = models.CharField(
		max_length=100,
		validators=[MinLengthValidator(2)],
		verbose_name="First name",
	)
	last_name = models.CharField(
		max_length=100,
		validators=[MinLengthValidator(2)],
		verbose_name="Last name",
	)
	email = models.EmailField(
		blank=True,
		null=True,
		verbose_name="Email",
	)
	phone = models.CharField(
		max_length=20,
		blank=True,
		null=True,
		verbose_name="Phone",
	)
	contact_type = models.CharField(
		max_length=20,
		choices=ContactType.CHOICES,
		default=ContactType.PERSON,
		db_index=True,
		verbose_name="Contact type",
	)
	company = models.CharField(
		max_length=150,
		blank=True,
		null=True,
		verbose_name="Company",
	)
	position = models.CharField(
		max_length=120,
		blank=True,
		null=True,
		verbose_name="Position",
	)
	notes = models.TextField(
		blank=True,
		null=True,
		verbose_name="Notes",
	)
	is_active = models.BooleanField(
		default=True,
		db_index=True,
		verbose_name="Is active",
	)
	created_at = models.DateTimeField(
		auto_now_add=True,
		verbose_name="Created at",
	)
	updated_at = models.DateTimeField(
		auto_now=True,
		verbose_name="Updated at",
	)

	class Meta:
		db_table = "contacts"
		verbose_name = "Contact"
		verbose_name_plural = "Contacts"
		ordering = ["-created_at"]
		indexes = [
			models.Index(fields=["contact_type"]),
			models.Index(fields=["is_active"]),
			models.Index(fields=["created_at"]),
		]

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name}".strip()
