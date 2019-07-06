import uuid

from decimal import Decimal
from django.db import models
from django.utils.timezone import now

from django.conf import settings


class FinancialReport(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Waived', 'Waived'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateField(default=now, null=True, blank=True)
    client_full_name = models.ForeignKey(settings.CLIENTS, on_delete=models.PROTECT)
    client_company_name = models.CharField(max_length=150)
    date_signed_up = models.DateField(default=now, null=True, blank=True)
    first_day_of_call = models.DateField(null=True, blank=True)
    first_billing_cycle = models.DateField(null=True, blank=True)
    last_billing_cycle = models.DateField(null=True, blank=True)
    type_of_plan = models.DecimalField(max_digits=7, decimal_places=2)
    total_minutes_used = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    excess_minutes = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
    payment_made = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    date_paid = models.DateField(default=now, null=True, blank=True)
    transaction_number = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    notes_inventory = models.TextField(null=True, blank=True, verbose_name="Notes")
    notes_payment_made = models.TextField(null=True, blank=True, verbose_name="Notes")

    class Meta:
        ordering = ['-date_signed_up']

    def __str__(self):
        return str(self.client_full_name)