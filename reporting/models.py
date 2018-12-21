import uuid
from django.conf import settings
from django.db import models
from fillables.models import ProjectManager, CompanyName, DateInformation, Task


class VATimeSheet(models.Model):
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
    month_to_date = models.CharField(max_length=10, choices=MONTH_TO_DATE_CHOICES, null=True, blank=True)
    date_information = models.ForeignKey(DateInformation, on_delete=models.PROTECT, null=True, blank=True)
    clients_full_name = models.ForeignKey(CompanyName, on_delete=models.PROTECT, null=True, blank=True)
    title_of_job_request = models.CharField(max_length=250, null=True, blank=True)
    list_of_task = models.ForeignKey(Task, on_delete=models.PROTECT, null=True, blank=True)
    job_request_description = models.TextField(null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    duration = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_items_finished = models.IntegerField(null=True, blank=True)
    additional_comments = models.TextField(null=True, blank=True)
    assigned_job_request_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.PROTECT, null=True, blank=True)
    approval_from_project_manager = models.CharField(max_length=100, choices=APPROVAL_CHOICES, null=True, blank=True)
    approval_of_admin = models.CharField(max_length=100, choices=APPROVAL_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = 'VA Time Sheet'
        verbose_name_plural = 'VA Time Sheets'
        ordering = ['clients_full_name']

    def __str__(self):
        return self.clients_full_name
