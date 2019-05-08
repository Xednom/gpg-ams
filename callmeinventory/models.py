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
    )
    date_of_call = models.DateField(default=now, null=True, blank=True)
    category = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    client_full_name = models.CharField(max_length=150, null=True, blank=True)
    client_company_name = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=150, null=True,blank=True)
    total_handling_time = models.DecimalField(max_digits=6, decimal_places=2)
    total_time_transferring_leads = models.DecimalField(max_digits=6, decimal_places=2)
    total_mins = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Call Me Inventory'
        verbose_name_plural = 'Call Me Inventories'
        ordering = ['-date_of_call']

    def calculate_time(self):
        total_time = self.total_handling_time + self.total_time_transferring_leads
        return total_time

    def save(self, *args, **kwargs):
        self.total_mins = self.calculate_time()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client_full_name +" of "+ self.client_company_name
