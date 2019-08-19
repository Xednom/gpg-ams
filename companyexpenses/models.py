from django.db import models
from django.utils.timezone import now


class Type(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Expenses(models.Model):
    TAGGING = (
        ('One Time', 'One Time'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly')
    )
    STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    )
    month = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=now, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=150)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.PROTECT)
    category = models.CharField(max_length=150, null=True, blank=True)
    tagging = models.CharField(max_length=150, choices=TAGGING, null=True, blank=True)
    next_due_date = models.DateField(default=now, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)
    payment_channel = models.CharField(max_length=150, null=True, blank=True)
    referrence = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "General Expense Inventory"
        verbose_name_plural = "General Expense Inventories"
        ordering = ['-date']
    
    def __str__(self):
        return str(self.type)




