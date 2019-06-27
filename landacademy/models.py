import uuid

from django.db import models
from django.utils.timezone import now


class LandAcademyInventory(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_completed = models.DateField(default=now, null=True, blank=True)
    date_paid = models.DateField(default=now, null=True, blank=True)
    pivot_table = models.URLField(null=True, blank=True)
    project_status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    payment_status = models.CharField(max_length=150, null=True, blank=True)
    invoice = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Land Academy Inventory Record'
        verbose_name_plural = 'Land Academy Inventory Records'
        ordering = ['-date_completed']

    def __str__(self):
        return self.invoice


class O20SmartPricing(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ('Complete Incorrect Data Input', 'Complete Incorrect Data Input'),
        ('Others', 'Others')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    situs_address = models.TextField(null=True, blank=True)
    trulia = models.CharField(max_length=150, null=True, blank=True)
    zillow = models.CharField(max_length=150, null=True, blank=True)
    redfin = models.CharField(max_length=150, null=True, blank=True)
    realfor = models.CharField(max_length=150, null=True, blank=True)
    realtytrac = models.CharField(max_length=150, null=True, blank=True)
    encoder = models.CharField(max_length=150, null=True, blank=True)
    date_encoded = models.DateField(default=now, null=True, blank=True)
    quality_check_status = models.CharField(max_length=25, choices=STATUS, null=True, blank=True)
    quality_specialist = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Land Academy O20 Smart Pricing'
        verbose_name_plural = 'Land Academy O20 Smart Pricings'
        ordering = ['-date_encoded']
    
    def __str__(self):
        return self.quality_specialist
