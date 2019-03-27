import uuid
from django.db import models

from fillables.models import ProjectManager, JobTitleRequest, VirtualAssistant


class JobRequest(models.Model):
    JOB_STATUS_CHOICES = (
        ('----', '------'),
        ('Complete', 'Complete'),
        ('in Progress', 'In Progress'),
        ('For Final Review', 'For Final Review'),
        ('Job Request Sent to VA', 'Job Request Sent to VA'),
    )
    MONTH_CHOICES = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    PROJECT_STATUS_CHOICES = (
        ('Sent to Project Manager', 'Sent to Project Manager'),
        ('Sent to Virtual Assistant', 'Sent to Virtual Assistant'),
        ('In Progress / PROCESSING', 'In Progress / PROCESSING'),
        ('Job Request Completed - VA Side', 'Job Request Completed - VA Side'),
        ('Submit to Project Manager for Quality Purposes', 'Submit to Project Manager for Quality Purposes'),
        ('Submit to Client', 'Submit to Client'),
        ('Job Request Completed', 'Job Request Completed'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=150, null=True, blank=True)
    date_requested = models.DateField(null=True, blank=True)
    month = models.CharField(max_length=150, choices=MONTH_CHOICES, null=True, blank=True)
    requestors_name = models.CharField(max_length=250, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    job_request_number = models.CharField(max_length=250, null=True, blank=True)
    job_request_title = models.CharField(max_length=150, null=True, blank=True)
    job_request_instruction = models.TextField(null=True, blank=True)
    additional_comments_or_feedbacks = models.TextField(null=True, blank=True)
    assigned_project_managers = models.ForeignKey(ProjectManager, on_delete=models.PROTECT, null=True, blank=True)
    project_status = models.CharField(max_length=150, choices=PROJECT_STATUS_CHOICES, null=True, blank=True)
    url_training_videos = models.URLField(null=True, blank=True)
    assigned_va = models.ForeignKey(VirtualAssistant, null=True, blank=True, on_delete=models.PROTECT)
    time_in = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2, default=0.00)
    time_out = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2, default=0.00)
    total_minutes_hours = models.IntegerField(null=True, blank=True)
    manager_notes = models.TextField(null=True, blank=True)
    client_notes = models.TextField(null=True, blank=True)
    va_notes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date_requested']

    def __str__(self):
        return str(self.job_request_title)
