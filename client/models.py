from django.conf import settings
from django.db import models
from uuid import uuid4


class CompanyCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return self.company_name


class ClientName(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    client_name = models.CharField(max_length=250)

    def __str__(self):
        return self.client_name


class Lead(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    lead_source = models.CharField(max_length=250)

    def __str__(self):
        return self.lead_source


class ProjectManager(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    project_manager = models.CharField(max_length=250)

    def __str__(self):
        return self.project_manager


class SeniorManager(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class TypeOfTask(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    task_name = models.CharField(max_length=250)

    def __str__(self):
        return self.task_name


class Client(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    date_sign_up = models.DateField()
    company_category_under = models.ForeignKey('CompanyCategory', on_delete=models.PROTECT)
    clients_company_name = models.CharField(max_length=250)
    agreed_hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    client = models.ForeignKey('Client', related_name='Client_name', on_delete=models.PROTECT)
    client_code = models.CharField(max_length=150)
    client_phone_number = models.CharField(max_length=150)
    client_email = models.EmailField(max_length=250)
    lead_source = models.ForeignKey('Lead', on_delete=models.PROTECT)
    referred_by = models.CharField(max_length=250)
    clients_project_manager = models.ForeignKey('ProjectManager', on_delete=models.PROTECT)
    clients_count_number = models.IntegerField()
    VA_assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
        )
    type_of_task = models.ForeignKey('TypeOfTask', on_delete=models.PROTECT)
    senior_manager = models.ForeignKey('SeniorManager', on_delete=models.PROTECT)
    notes = models.TextField()

    def __str__(self):
        return self.client
