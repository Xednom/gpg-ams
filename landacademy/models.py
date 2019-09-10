import uuid

from decimal import Decimal
from django.db import models
from django.utils.timezone import now
from django.conf import settings


class LandAcademyInventory(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    )
    PAYMENT = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_requested = models.DateField(default=now, null=True, blank=True)
    date_completed = models.DateField(default=now, null=True, blank=True)
    date_payment_made = models.DateField(default=now, null=True, blank=True)
    order_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="Order Name/Number")
    client_la_requestor = models.CharField(max_length=250, null=True, blank=True, verbose_name="Client LA Requestor")
    complete_order = models.CharField(max_length=150, null=True, blank=True, verbose_name="Complete Order - URL Link")
    status_of_order = models.CharField(max_length=150, choices=STATUS, null=True, blank=True, verbose_name="Status of the Order")
    payment_status = models.CharField(max_length=150, choices=PAYMENT, null=True, blank=True)
    invoice = models.CharField(max_length=150, null=True, blank=True, verbose_name="Invoice # Towards LA")
    total_items_charge = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Total Charge", help_text="Total Items Requested x $.06")
    total_pp_fee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Total PP Fee", help_text="Total Charge *.05")
    total_charge = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, help_text="Total Charge + Total PP Fee")
    total_items_requested = models.PositiveIntegerField(default=0, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Land Academy Inventory Record'
        verbose_name_plural = 'Land Academy Inventory Records'
        ordering = ['-date_completed']

    def __str__(self):
        return self.invoice

    def calculation_total_items_charged(self):
        percent = .06
        items = self.total_items_requested*Decimal(percent)
        total_items = Decimal(items)
        return total_items
    
    def calculation_pp_fee(self):
        percent = .05
        fee = self.calculation_total_items_charged()*Decimal(percent)
        pp_fee = Decimal(fee)
        return pp_fee
    
    def calculation_total_charge(self):
        total = self.calculation_total_items_charged() + self.calculation_pp_fee()
        total = Decimal(total)
        return total
    
    def save(self, *args, **kwargs):
        self.total_items_charge = self.calculation_total_items_charged()
        self.total_pp_fee = self.calculation_pp_fee()
        self.total_charge = self.calculation_total_charge()
        super().save(*args, **kwargs)


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
    order_name = models.CharField(max_length=150, null=True, blank=True)
    requestor_full_name = models.CharField(max_length=150, default="Jack Butala")
    researcher_name = models.ForeignKey(settings.STAFFS, null=True, blank=True, \
                                        on_delete=models.PROTECT, related_name='researcher')
    date_requested = models.DateField(default=now, null=True, blank=True)
    date_research = models.DateField(default=now, null=True, blank=True)
    date_encoded = models.DateField(default=now, null=True, blank=True)
    quality_check_status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    quality_specialist = models.ForeignKey(settings.STAFFS, null=True, blank=True, \
                                           on_delete=models.PROTECT, related_name='QA')
    notes_from_researcher = models.TextField(null=True, blank=True, verbose_name="Notes From the Researcher")
    notes_from_qa = models.TextField(null=True, blank=True, verbose_name="Notes From the QA Specialist")

    class Meta:
        verbose_name = 'Land Academy O20 Smart Pricing'
        verbose_name_plural = 'Land Academy O20 Smart Pricings'
        ordering = ['-date_encoded']
    
    def __str__(self):
        return str(self.quality_specialist)
