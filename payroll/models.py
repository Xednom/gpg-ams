import uuid

from decimal import Decimal
from django.db import models
from django.utils import timezone as tz
from django.urls import reverse

from fillables.models import VirtualAssistant

# Create your models here.
class VaPayroll(models.Model):
    STATUS_CHOICES = (
        ('APPROVED-BY-THE-MANAGER', 'Approved by the Manager'),
        ('HOURS-RE-ADJUSTMENT', 'Hours Re-Adjustment'),
        ('DECLINED', 'Declined'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    virtual_assistant = models.CharField(max_length=150, null=True, blank=True)
    time_in = models.DateTimeField(default=tz.now, null=True, blank=True)
    time_out = models.DateTimeField(default=tz.now, null=True, blank=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    client_name = models.CharField(max_length=150, null=True, blank=True)
    rate = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, help_text="Salary = Total hours * Hourly rate")
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'VA Payroll'
        verbose_name_plural = 'VA Payrolls'
        ordering = ['date']

    def calculate_salary(self):
        worked_hours = (self.time_out - self.time_in).total_seconds() / 60 / 60
        total_salary = Decimal(worked_hours) * self.rate
        # salary = round((total_salary, 0) * self.rate)
        return total_salary

    def calculate_working_hours(self):
        worked_hours = (self.time_out - self.time_in).total_seconds() / 60 / 60
        total_hours = Decimal(worked_hours)
        return total_hours

    def save(self, *args, **kwargs):
        self.salary = self.calculate_salary()
        self.hours = self.calculate_working_hours()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('payroll:add_payroll')
    
    def __str__(self):
        return str(self.virtual_assistant)
