import uuid
import datetime
from django.db import models


class JobTitleRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'List of Job title request'
        verbose_name_plural = 'List of Job title requests'
        ordering = ['-title']

    def __str__(self):
        return self.title


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
        return self.name + ', Code: ' + self.code


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

    class Meta:
        verbose_name = 'List of Type of Task'
        verbose_name_plural = 'List of Type of Tasks'

    def __str__(self):
        return self.task_name


class DateInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    weeks = models.CharField(max_length=250)

    def __str__(self):
        return self.weeks


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_name = models.CharField(max_length=250)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'List of Task'
        verbose_name_plural = 'List of Tasks'

    def __str__(self):
        return self.job_name
