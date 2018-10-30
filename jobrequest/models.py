import uuid
from django.db import models
from client.models import ProjectManager


class JobRequest(models.Model):
    STATUS_OF_JOB_REQUEST = (
        ('FOR FINAL REVIEW', 'For Final Review'),
        ('JOB REQUEST SENT TO VA', 'Job Request sent to VA'),
        ('IN PROGRESS', 'In Progress'),
        ('COMPLETE', 'Complete')
    )

    date = models.DateField()
    due_date = models.DateField()
    client_code = models.CharField(max_length=250)
    job_request_title = models.CharField(max_length=250, default='Give me a title later')
    job_request_sent_via = models.CharField(max_length=250)
    job_request_instruction = models.TextField()
    total_hours_minutes_allocated = models.DecimalField(max_digits=4, decimal_places=2)
    project_managers = models.ForeignKey('client.ProjectManager', default='Gillian', on_delete=models.PROTECT)
    VA_admin_support = models.CharField(max_length=250)
    status_of_the_job_request = models.CharField(max_length=250, default='----', choices=STATUS_OF_JOB_REQUEST)
    notes_and_coaching_from_project_manager = models.TextField()
