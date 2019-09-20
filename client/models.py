import uuid
from django.conf import settings
from django.db import models
from django.utils.timezone import now

from fillables.models import (
                            InternalCompanyName, CompanyName, LeadSource,
                            ProjectManager, SeniorManager, TypeOfTask
                            )


class Client(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_sign_up = models.DateField(null=True, blank=True)
    company_category_under = models.ForeignKey(InternalCompanyName, on_delete=models.PROTECT, null=True, blank=True)
    client_company_name = models.CharField(max_length=250, null=True, blank=True)
    agreed_hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    company_name = models.ForeignKey(CompanyName, verbose_name="Client Owner's Name", on_delete=models.PROTECT, null=True, blank=True)
    client_code = models.CharField(max_length=150, null=True, blank=True)
    client_phone_number = models.CharField(max_length=150, null=True, blank=True)
    client_email = models.EmailField(max_length=250, null=True, blank=True)
    lead_source = models.ForeignKey(LeadSource, on_delete=models.PROTECT, null=True, blank=True)
    referred_by = models.CharField(max_length=250, null=True, blank=True)
    clients_project_manager = models.ForeignKey(ProjectManager, on_delete=models.PROTECT, null=True, blank=True)
    clients_count_number = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    VA_assigned = models.ForeignKey(
        settings.STAFFS,
        on_delete=models.PROTECT,
        null=True, blank=True
        )
    type_of_task = models.ForeignKey(TypeOfTask, on_delete=models.PROTECT, null=True, blank=True)
    senior_manager = models.ForeignKey(SeniorManager, on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'List of Client Job'
        verbose_name_plural = 'List of Client Jobs'
        ordering = ['-date_sign_up']

    def __str__(self):
        return str(self.company_name)


class ClientLeadSource(models.Model):
    LEAD = (
        ('Craiglists', 'Craiglists'),
        ('Facebook', 'Facebook'),
        ('KSL.Com', 'KSL.Com'),
        ('Website', 'Website'),
        ('LandPin', 'LandPin'),
        ('Zillow', 'Zillow'),
        ('LandandFarm', 'LandandFarm'),
        ('Lands of America', 'Lands of America'),
        ('Facebook', 'Facebook'),
        ('Facebook Marketplace', 'Facebook Marketplace'),
        ('Property Control Center', 'Property Control Center'),
        ('Neighbor Letters', 'Neighbor Letters'),
        ('Mailchimp', 'Mailchimp'),
        ('Landstay', 'Landstay'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('Others', 'Others')
    )
    STATUS = (
        ('Dead Lead', 'Dead Lead'),
        ('Hot Leads', 'Hot Leads'),
        ('Requires Follow up', 'Requires Follow up'),
        ('Interested', 'Interested'),
        ('Not Interested', 'Not Interested'),
        ('Inquires Only', 'Inquires Only'),
        ('Others', 'Others'),
        ('Closed Sale', 'Closed Sale'),

    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_lead_received = models.DateField(null=True, blank=True, default=now)
    client = models.ForeignKey(settings.CLIENTS, on_delete=models.PROTECT)
    lead_source = models.CharField(max_length=150, choices=LEAD, null=True, blank=True)
    full_name_of_lead = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    type_of_lead = models.CharField(max_length=150, null=True, blank=True)
    lead_profile_url = models.CharField(max_length=150, null=True, blank=True)
    lead_profile_under = models.CharField(max_length=150, null=True, blank=True)
    lead_status = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    virtual_assistant = models.ForeignKey(settings.STAFFS, null=True, blank=True, on_delete=models.PROTECT)
    notes_from_client = models.TextField(null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)
    others = models.CharField(max_length=150, null=True, blank=True, help_text="If Lead source is 'Others' please fill this.")

    class Meta:
        verbose_name = 'Clients Lead Source Inventory'
        verbose_name_plural = 'Clients Lead Source Inventories'
        ordering = ['-date_lead_received']
    
    def __str__(self):
        return '%s' % (self.client)
