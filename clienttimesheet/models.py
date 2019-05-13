import uuid

from decimal import Decimal
from django.db import models
from django.utils.timezone import now

from fillables.models import VirtualAssistant


class TimeSheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_tagging = models.CharField(max_length=150, null=True, blank=True)
    shift_date = models.DateField(default=now, null=True, blank=True)
    month_to_date = models.DateField(default=now, null=True, blank=True)
    clients_full_name = models.CharField(max_length=150, null=True, blank=True)
    title_job_request = models.CharField(max_length=150, null=True, blank=True)
    job_request = models.CharField(max_length=150, null=True, blank=True)
    time_in = models.DateTimeField(default=now, null=True, blank=True)
    time_out = models.DateTimeField(default=now, null=True, blank=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_items = models.CharField(max_length=150, null=True, blank=True)
    additional_comments = models.TextField(null=True, blank=True)
    assigned_job_request_to = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    amount_charge = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tax_fee = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_tax_fee = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    total_amount_due = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Client TimeSheet"
        verbose_name_plural = "Client TimeSheets"
        ordering = ['-company_tagging']

    def __str__(self):
        return self.company_tagging

    def calculate_hours(self):
        total_hours = (self.time_out - self.time_in).total_seconds() / 60 / 60
        total_duration = Decimal(total_hours)
        return total_duration
    
    def calculate_amount_charge(self):
        charge = self.duration * self.hourly_rate
        total_charge = Decimal(charge)
        return total_charge

    def calculate_total_tax_fee(self):
        amount = self.amount_charge * self.tax_fee
        total_tax = Decimal(amount)
        return total_tax

    def calculate_total_amount(self):
        amount = self.amount_charge + self.total_tax_fee
        total_amount = Decimal(amount)
        return total_amount

    def save(self, *args, **kwargs):
        self.duration = self.calculate_hours()
        self.amount_charge = self.calculate_amount_charge()
        self.total_tax_fee = self.calculate_total_tax_fee()
        self.total_amount_due = self.calculate_total_amount()
        super().save(*args, **kwargs)


class PaymentMade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(default=now, null=True, blank=True, help_text="Date the payment made.")
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    reference = models.CharField(max_length=150, null=True, blank=True)
    payment_channel = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Payment Made for the Client"
        verbose_name_plural = "Payment Made for the Clients"
        ordering = ['-date']

    def __str__(self):
        return self.date