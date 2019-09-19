import uuid

from django.conf import settings

from decimal import Decimal
from django.db import models
from django.db.models import F
from django.utils.timezone import now


class inventory(models.Model):
    CATEGORY = (
        ('Buyers', 'Buyers'),
        ('Sellers', 'Sellers'),
        ('General Call', 'General Call'),
        ('Voicemail', 'Voicemail'),
        ('Property Management', 'Property Management'),
        ('Others', 'Others'),
    )
    STATUS = (
        ('New', 'New'),
        ('Transferred to Podio - Personal Account',
         'Transferred to Podio - Personal Account'),
        ('Transferred to Land Speed', 'Transferred to Land Speed'),
        ('Transferred to Investment Dominator',
         'Transferred to Investment Dominator'),
        ('Transferred to Buildium', 'Transferred to Buildium'),
        ('Airtable', 'Airtable'),
        ('Others', 'Others'),
    )
    FINANCIAL = (
        ('Billed', 'Billed'),
        ('Unbilled', 'Unbilled'),
        ('Waived', 'Waived')
    )
    LEAD = (
        ('Interested', 'Interested'),
        ('Not Interested', 'Not Interested'),
        ('Dead Lead', 'Dead Lead'),
        ('Others', 'Others')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transferred_date = models.DateField(default=now, null=True, blank=True)
    date_lead_received = models.DateField(default=now, null=True, blank=True)
    type_of_form = models.CharField(
        max_length=150, choices=CATEGORY, null=True, blank=True)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    full_name_of_lead = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    customer_representative = models.CharField(
        max_length=150, null=True, blank=True)
    status = models.CharField(
        max_length=150, choices=STATUS, null=True, blank=True)
    lead_transferred_by = models.CharField(
        max_length=150, null=True, blank=True)
    financial_status = models.CharField(
        max_length=150, choices=FINANCIAL, null=True, blank=True)
    call_duration = models.DecimalField(max_digits=6, decimal_places=2)
    total_time_transferring_leads = models.DecimalField(
        max_digits=6, decimal_places=2)
    total_mins = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    lead_conversion = models.CharField(
        max_length=150, choices=LEAD, null=True, blank=True)

    class Meta:
        verbose_name = 'Call Me Inventory'
        verbose_name_plural = 'Call Me Inventories'
        ordering = ['-transferred_date']

    def calculate_time(self):
        total_time = self.call_duration + self.total_time_transferring_leads
        return total_time

    def save(self, *args, **kwargs):
        self.total_mins = self.calculate_time()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.client_full_name)


class VaForm(models.Model):
    SCRIPT = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
        ('Propert Management', 'Propert Management'),
        ('General Calls', 'General Calls')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    client_full_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True,
                                         on_delete=models.PROTECT)
    type_of_script = models.CharField(max_length=150, choices=SCRIPT, null=True, blank=True)
    script_link = models.CharField(max_length=500, null=True, blank=True)
    gs_integration = models.CharField(max_length=250, null=True, blank=True)
    client_call_forwarding_number = models.CharField(max_length=150, null=True, blank=True)
    company_call_forwarding_number = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s' % (self.client_full_name)

