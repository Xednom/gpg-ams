import uuid

from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models import F
from django.utils.timezone import now



class inventory(models.Model):
    CATEGORY = (
        ('Buyers', 'Buyers'),
        ('Sellers', 'Sellers'),
        ('General Call', 'General Call'),
        ('Voicemail', 'Voicemail'),
    )
    STATUS = (
        ('New', 'New'),
        ('Transferred to Podio - Personal Account', 'Transferred to Podio - Personal Account'),
        ('Transferred to Land Speed', 'Transferred to Land Speed'),
        ('Transferred to Investment Dominator ', 'Transferred to Investment Dominator '),
        ('Airtable ', 'Airtable '),
        ('Others', 'Others'),
    )
    FINANCIAL = (
        ('Billed', 'Billed'),
        ('Unbilled', 'Unbilled'),
        ('Waived', 'Waived')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transferred_date = models.DateField(default=now, null=True, blank=True)
    date_lead_received = models.DateField(default=now, null=True, blank=True)
    type_of_form = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    client_company_name = models.CharField(max_length=150, null=True, blank=True)
    full_name_of_lead = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    customer_representative = models.OneToOneField(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    financial_status = models.CharField(max_length=150, choices=FINANCIAL, null=True, blank=True)
    call_duration = models.DecimalField(max_digits=6, decimal_places=2)
    total_time_transferring_leads = models.DecimalField(max_digits=6, decimal_places=2)
    total_mins = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

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
        return self.client_full_name +" of "+ self.client_company_name
