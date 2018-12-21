import uuid
from django.db import models

from fillables.models import ProjectManager, JobTitleRequest


class JobRequest(models.Model):
    JOB_STATUS_CHOICES = (
        ('----', '------'),
        ('complete', 'Complete'),
        ('in-progress', 'In Progress'),
        ('for-final-review', 'For Final Review'),
        ('job-request-sent-to-va', 'Job Request Sent to VA'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    client_code = models.CharField(max_length=250)
    job_request_title = models.ForeignKey(JobTitleRequest, on_delete=models.PROTECT, null=True, blank=True)
    job_request_sent_via = models.CharField(max_length=250, null=True, blank=True)
    job_request_instruction = models.TextField()
    total_hours_minutes_allocated = models.CharField(max_length=100, null=True, blank=True)
    project_managers = models.ForeignKey(ProjectManager, on_delete=models.PROTECT, null=True, blank=True)
    VA_admin_support = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=100, default='----', choices=JOB_STATUS_CHOICES)
    notes_and_coaching_from_project_manager = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.job_request_title)
