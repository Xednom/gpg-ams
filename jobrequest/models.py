import uuid
from django.db import models
from decimal import Decimal
from django.utils.timezone import now

from users.models import Staffs, Clients

from fillables.models import (
    ProjectManager, 
    JobTitleRequest, 
    VirtualAssistant,
    CompanyName,
    InternalCompanyName
    )



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
    CATEGORY = (
        ('General Administrative Task', 'General Administrative Task'),
        ('Data Entry', 'Data Entry'),
        ('Website Design', 'Website Design'),
        ('Graphics Design', 'Graphics Design'),
        ('Customer Support', 'Customer Support'),
        ('Creating Ad Content', 'Creating Ad Content'),
        ('Marketing', 'Marketing'),
        ('Due Diligence', 'Due Diligence'),
        ('Craigslist Support', 'Craigslist Support'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_to_request = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    category = models.CharField(max_length=150, choices=CATEGORY, null=True, blank=True)
    date_requested = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    month = models.CharField(max_length=150, choices=MONTH_CHOICES, null=True, blank=True)
    requestors_name = models.CharField(max_length=250, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    job_request_title = models.CharField(max_length=150, null=True, blank=True)
    job_request_instruction = models.TextField(null=True, blank=True)
    additional_comments_or_feedbacks = models.TextField(null=True, blank=True)
    assigned_project_managers = models.ForeignKey(Staffs, on_delete=models.PROTECT, null=True, blank=True, related_name='PMs')
    project_status = models.CharField(max_length=150, choices=PROJECT_STATUS_CHOICES, null=True, blank=True)
    url_training_videos = models.CharField(max_length=250, null=True, blank=True)
    assigned_va = models.ForeignKey(Staffs, null=True, blank=True, on_delete=models.PROTECT, related_name='VAs')
    manager_notes = models.TextField(null=True, blank=True)
    client_notes = models.TextField(null=True, blank=True)
    va_notes = models.TextField(null=True, blank=True)
    company_tagging = models.ForeignKey(InternalCompanyName, null=True, blank=True, on_delete=models.PROTECT)
    authorized_minutes_hours_allocation = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date_requested']

    def __str__(self):
        return str(self.job_request_title)


class JobRequestTimeSheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.ForeignKey(JobRequest, on_delete=models.PROTECT, related_name="timesheet")
    staff = models.ForeignKey(Staffs, null=True, blank=True, on_delete=models.PROTECT, related_name="Staffs")
    client = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.PROTECT, related_name="Clients")
    time_in = models.DateTimeField(default=now, null=True, blank=True)
    time_out = models.DateTimeField(default=now, null=True, blank=True)
    total_minutes_hours = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.job_title)

    def calculate_working_hours(self):
        worked_hours = (self.time_out - self.time_in).total_seconds() / 60 / 60
        total_hours = Decimal(worked_hours)
        return total_hours

    def save(self, *args, **kwargs):
        self.total_minutes_hours = self.calculate_working_hours()
        super().save(*args, **kwargs)
