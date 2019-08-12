import uuid

from django.utils.timezone import now
from django.db import models
from django.conf import settings


class CraiglistInventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name_company_name = models.ForeignKey(settings.CLIENTS, null=True, 
                                            blank=True, on_delete=models.PROTECT)
    cl_admin_support = models.ForeignKey(settings.STAFFS, null=True, 
                                         blank=True, on_delete=models.PROTECT)
    date = models.DateField(null=True, blank=True)
    posted_ads = models.CharField(max_length=150, null=True, blank=True)
    flagged_ads = models.CharField(max_length=150, null=True, blank=True)
    sticked_ads = models.CharField(max_length=150, null=True, blank=True)
    stick_rates = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Craigslist Inventory Record'
        verbose_name_plural = 'Craigslist Inventory Records'
        ordering = ['-date']

    def __str__(self):
        return self.client_company_name