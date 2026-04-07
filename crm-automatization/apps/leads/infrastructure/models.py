from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from apps.leads.domain.constants import LeadSource, LeadStatus


class Lead(models.Model):
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
    status = models.CharField(
        max_length=20,
        choices=LeadStatus.CHOICES,
        default=LeadStatus.NEW,
        db_index=True,
        verbose_name="Status",
    )
    source = models.CharField(
        max_length=20,
        choices=LeadSource.CHOICES,
        default=LeadSource.OTHER,
        db_index=True,
        verbose_name="Source",
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Notes",
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="assigned_leads",
        verbose_name="Assigned to",
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
        db_table = "leads"
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["source"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["assigned_to"]),
        ]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()