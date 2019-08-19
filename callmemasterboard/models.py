import uuid

from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class MasterBoard(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Ready to Start', 'Ready to Start'),
        ('For Follow-up', 'For Follow-up'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_started = models.DateField(default=now, null=True, blank=True)
    due_date = models.DateField(default=now, null=True, blank=True)
    type_of_plan = models.CharField(max_length=150, null=True, blank=True)
    type_of_crm = models.CharField(max_length=150, null=True, blank=True)
    type_of_voip = models.CharField(max_length=150, null=True, blank=True)
    client_name = models.ForeignKey(settings.CLIENTS, null=True, blank=True, on_delete=models.PROTECT)
    url_buyer = models.CharField(max_length=250, null=True, blank=True)
    url_seller = models.CharField(max_length=250, null=True, blank=True)
    url_property_management = models.CharField(max_length=250, null=True, blank=True)
    voicemail = models.CharField(max_length=150, null=True, blank=True)
    general_calls = models.CharField(max_length=150, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    gs_integration = models.TextField(null=True, blank=True, verbose_name="GS Integration")
    client_folder = models.TextField(null=True, blank=True, verbose_name="Clients's Folder")
    email = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    phone_login = models.TextField(null=True, blank=True, verbose_name="Phone System - Log In Information")
    crm_login = models.TextField(null=True, blank=True, verbose_name="CRM System - Log In Information")
    call_forwarding_details = models.TextField(null=True, blank=True)
    email_form_forwarding = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)
    monthly_plan_cost = models.CharField(max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name = 'CallMe Master Board'
        verbose_name_plural = 'CallMe Master Boards'
        ordering = ['-date_started']
    
    def __str__(self):
        return str(self.client_name)
