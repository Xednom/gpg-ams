import uuid

from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class MasterBoard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_started = models.DateField(default=now, null=True, blank=True)
    type_of_plan = models.CharField(max_length=150, null=True, blank=True)
    type_of_crm = models.CharField(max_length=150, null=True, blank=True)
    type_of_voip = models.CharField(max_length=150, null=True, blank=True)
    client_name = models.OneToOneField(settings.CLIENTS, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    url_buyer = models.URLField(null=True, blank=True)
    url_seller = models.URLField(null=True, blank=True)
    url_property_management = models.URLField(null=True, blank=True)
    voicemail = models.CharField(max_length=150, null=True, blank=True)
    general_calls = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'CallMe Master Board'
        verbose_name_plural = 'CallMe Master Boards'
        ordering = ['-date_started']
    
    def __str__(self):
        return str(self.client_name)
