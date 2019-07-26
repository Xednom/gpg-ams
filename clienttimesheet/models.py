import uuid

from decimal import Decimal
from django.conf import settings

from djmoney.models.fields import MoneyField
from django.db import models
from django.utils.timezone import now

from fillables.models import VirtualAssistant


class TimeSheet(models.Model):
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )
    STATUS = (
        ('Approved', 'Approved'),
        ('For Review', 'For Review'),
        ('Dispute', 'Dispute'),
        ('Waived', 'Waived'),
    )
    APPROVAL = (
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Dispute', 'Dispute'),
        ('Waived', 'Waived'),
    )
    COMPANY_TAGGING = (
        ('landmaster.us', 'landmaster.us'),
        ('gpgcorporation.com', 'gpgcorporation.com'),
        ('callme.com.ph', 'callme.com.ph'),
        ('virtualExpressServices.com', 'virtualExpressServices.com'),
        ('creatif-designs.com', 'creatif-designs.com'),
        ('vacantpropertiesglobal.com', 'vacantpropertiesglobal.com')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_tagging = models.CharField(max_length=150, choices=COMPANY_TAGGING,
                                       null=True, blank=True)
    shift_date = models.DateField(default=now, null=True, blank=True)
    month_to_date = models.CharField(max_length=150, choices=MONTH, null=True, blank=True)
    clients_full_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True,
                                          on_delete=models.PROTECT)
    title_job_request = models.CharField(max_length=150, null=True, blank=True)
    channel_job_requested = models.CharField(max_length=150, null=True, blank=True)
    job_request_description = models.TextField(null=True, blank=True)
    time_in = models.DateTimeField(default=now, null=True, blank=True)
    time_out = models.DateTimeField(default=now, null=True, blank=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_items = models.CharField(max_length=150, null=True, blank=True)
    additional_comments = models.TextField(null=True, blank=True)
    assigned_va = models.ForeignKey(settings.STAFFS, null=True, blank=True, 
                                    on_delete=models.PROTECT,
                                    verbose_name='Assigned VA',
                                    related_name='vas')
    assigned_pm = models.ForeignKey(settings.STAFFS, null=True, blank=True, 
                                    on_delete=models.PROTECT,
                                    verbose_name='Assigned Project Manager',
                                    related_name='pms')
    hourly_rate_peso = models.DecimalField(max_digits=7, decimal_places=2,
                                           default=0.00, null=True, blank=True)
    hourly_rate_usd = models.DecimalField(max_digits=14, decimal_places=2, 
                                          default=0.00, null=True, blank=True)
    total_charge_peso = models.DecimalField(max_digits=7, decimal_places=2,
                                            default=0.00, null=True, blank=True)
    total_charge_usd = models.DecimalField(max_digits=7, decimal_places=2,     
                                           default=0.00, null=True, blank=True)
    paypal_charge = models.DecimalField(max_digits=7, decimal_places=2,
                                        default=0.05, null=True, blank=True)
    total_charge_with_paypal = models.DecimalField(max_digits=7, decimal_places=2,
                                                   default=0.00, null=True, blank=True)
    total_amount_due = models.DecimalField(max_digits=7, decimal_places=2,
                                           default=0.00, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[1][1])
    admin_approval = models.CharField(max_length=50, choices=APPROVAL, default=STATUS[1][1])

    class Meta:
        verbose_name = "General Timesheet"
        verbose_name_plural = "General Timesheets"
        ordering = ['-shift_date']

    def __str__(self):
        return self.company_tagging

    def calculate_total_duration(self):
        total_hours = (self.time_out - self.time_in).total_seconds() / 60 / 60
        total_duration = Decimal(total_hours)
        return total_duration
    
    def calculate_total_charge_peso(self):
        charge = self.duration * self.hourly_rate_peso
        total_charge = Decimal(charge)
        return total_charge

    def calculate_total_charge_usd(self):
        charge = self.duration * self.hourly_rate_usd
        total_charge = Decimal(charge)
        return total_charge
    
    def calculate_total_charge_w_paypal(self):
        charge = Decimal(self.total_charge_usd) * Decimal(self.paypal_charge)
        total_charge = Decimal(charge)
        return total_charge

    def calculate_total_amount_due(self):
        amount_due = self.total_charge_usd + self.total_charge_with_paypal
        total_amount_due = Decimal(amount_due)
        return total_amount_due

    def save(self, *args, **kwargs):
        self.duration = self.calculate_total_duration()
        self.total_charge_peso = self.calculate_total_charge_peso()
        self.total_charge_usd = self.calculate_total_charge_usd()
        self.total_charge_with_paypal = self.calculate_total_charge_w_paypal()
        self.total_amount_due = self.calculate_total_amount_due()
        super().save(*args, **kwargs)


class PaymentMade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True,
                                    on_delete=models.PROTECT)
    date = models.DateField(default=now, null=True, blank=True, 
                            help_text="Date payment made.")
    amount = MoneyField(max_digits=14, decimal_places=2, null=True, blank=True)
    transaction_number = models.CharField(max_length=150, null=True, blank=True)
    payment_channel = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Payment Made for the Client"
        verbose_name_plural = "Payment Made for the Clients"
        ordering = ['-date']

    def __str__(self):
        return str(self.date)


class CashOut(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(settings.STAFFS, null=True, blank=True,
                             on_delete=models.PROTECT)
    cash_date_release = models.DateField(default=now, null=True, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2, null=True, blank=True)
    reference = models.CharField(max_length=150, null=True, blank=True)
    rcbc = models.CharField(max_length=150, null=True, blank=True,
                            verbose_name='RCBC')
    approved_by = models.CharField(max_length=150, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-cash_date_release']

    def __str__(self):
        return self.reference
