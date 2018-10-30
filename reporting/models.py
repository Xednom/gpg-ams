import uuid
from django.conf import settings
from django.db import models
from client.models import ProjectManager


class WeekToDate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    weeks = models.CharField(max_length=250)

    def __str__(self):
        return self.weeks


class ClientName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_name = models.CharField(max_length=250)

    def __str__(self):
        return self.job_name


class Report(models.Model):
    MONTH_TO_DATE_CHOICES = (
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')
    )
    APPROVAL_CHOICES = (
        ('APPROVED', 'Approved'),
        ('FOR REVIEW', 'For Review')
    )

    shift_date = models.DateField()
    month_to_date = models.CharField(max_length=10, choices=MONTH_TO_DATE_CHOICES)
    week_to_date = models.ForeignKey('WeekToDate', on_delete=models.PROTECT)
    clients_full_name = models.ForeignKey('ClientName', on_delete=models.PROTECT)
    title_of_job_request = models.CharField(max_length=250)
    job_requested_from = models.ForeignKey('Job', on_delete=models.PROTECT)
    job_request_description = models.TextField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    total_items_finished = models.IntegerField()
    additional_comments = models.TextField()
    assigned_job_request_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    project_manager = models.ForeignKey('client.ProjectManager', null=True, blank=True, on_delete=models.PROTECT)
    approval_from_project_manager = models.CharField(max_length=100, choices=APPROVAL_CHOICES)
    approval_of_admin = models.CharField(max_length=100, choices=APPROVAL_CHOICES)

    def __str__(self):
        return self.clients_full_name
