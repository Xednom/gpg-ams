import uuid
import datetime

from decimal import Decimal
from django.db import models
from django.utils.timezone import now


class CallMe(models.Model):
    CATEGORY=(
        ('Buyers', 'Buyers'),
        ('Sellers', 'Sellers'),
        ('General Call', 'General Call'),
        ('Voicemail', 'Voicemail')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(default=now, null=True, blank=True, help_text="Date of the call.")
    category = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    client_name = models.CharField(max_length=150, null=True, blank=True, help_text="Client Full name")
    company_name = models.CharField(max_length=150, null=True, blank=True, help_text="Client's company name")
    mobile = models.CharField(max_length=150, null=True, blank=True, help_text="Mobile number")
    total_handling_time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_transferring_leads = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_mins = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Call me Inventory"
        verbose_name_plural = "Call me Inventories"
        ordering = ['-date']
    
    def calculate_time(self):
        minutes = self.total_handling_time + self.total_transferring_leads
        total_minutes = Decimal(minutes)
        return total_minutes
    
    def save(self, *args, **kwargs):
        self.total_mins = self.calculate_time()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.client_name


