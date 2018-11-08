import uuid
from django.db import models
from client.models import ProjectManager


class StatusOfTheJobRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_of_status = models.CharField(max_length=250)

    def __str__(self):
        return self.type_of_status


class JobRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    client_code = models.CharField(max_length=250)
    job_request_title = models.CharField(max_length=250, default='Give me a title later')
    job_request_sent_via = models.CharField(max_length=250)
    job_request_instruction = models.TextField()
    total_hours_minutes_allocated = models.DecimalField(max_digits=4, decimal_places=2)
    project_managers = models.ForeignKey('client.ProjectManager', default='Gillian', on_delete=models.PROTECT)
    VA_admin_support = models.CharField(max_length=250)
    status_of_the_job_request = models.ForeignKey('StatusOfTheJobRequest', on_delete=models.PROTECT)
    notes_and_coaching_from_project_manager = models.TextField()

    def __str__(self):
        return self.job_request_title
