import uuid
from django.conf import settings
from django.db import models


class InternalCompanyName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Internal Company Names"

    def __str__(self):
        return self.company_name


class CompanyName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Company name'
        verbose_name_plural = 'Company names'

    def __str__(self):
        return self.name + self.code


class LeadSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lead_source = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Lead Source'
        verbose_name_plural = 'Lead Sources'

    def __str__(self):
        return self.lead_source


class ProjectManager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_manager = models.CharField(max_length=250)

    def __str__(self):
        return self.project_manager


class SeniorManager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class TypeOfTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.task_name


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
    company_name = models.ForeignKey(CompanyName, related_name='CompanyName', verbose_name="Client Owner's Name", on_delete=models.PROTECT, null=True, blank=True)
    client_code = models.CharField(max_length=150, null=True, blank=True)
    client_phone_number = models.CharField(max_length=150, null=True, blank=True)
    client_email = models.EmailField(max_length=250, null=True, blank=True)
    lead_source = models.ForeignKey(LeadSource, on_delete=models.PROTECT, null=True, blank=True)
    referred_by = models.CharField(max_length=250, null=True, blank=True)
    clients_project_manager = models.ForeignKey('ProjectManager', on_delete=models.PROTECT, null=True, blank=True)
    clients_count_number = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    VA_assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True, blank=True
        )
    type_of_task = models.ForeignKey('TypeOfTask', on_delete=models.PROTECT, null=True, blank=True)
    senior_manager = models.ForeignKey('SeniorManager', on_delete=models.PROTECT, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'List of Client'
        verbose_name_plural = 'List of Clients'
        ordering = ['-date_sign_up']

    def __str__(self):
        return str(self.client)
