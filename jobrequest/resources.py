from import_export import resources
from import_export.fields import Field

from .models import JobRequest


class JobRequestResource(resources.ModelResource):

    class Meta:
        model = JobRequest
        fields = (
            'date_requested', 'due_date',
            'company_to_request', 'category',
            'month', 'requestors_name',
            'company_name', 'job_request_title', 'job_request_instruction',
            'additional_comments_or_feedbacks', 'assigned_project_managers__full_name',
            'project_status', 'url_training_videos', 'assigned_va__full_name', 'manager_notes',
            'client_notes', 'va_notes', 'company_tagging__company_name', 'authorized_minutes_hours_allocation'
        )
        export_order = (
            'date_requested', 'due_date',
            'company_to_request', 'category',
            'month', 'requestors_name',
            'company_name', 'job_request_title', 'job_request_instruction',
            'additional_comments_or_feedbacks', 'assigned_project_managers__full_name',
            'project_status', 'url_training_videos', 'assigned_va__full_name', 'manager_notes',
            'client_notes', 'va_notes', 'company_tagging__company_name', 'authorized_minutes_hours_allocation'
        )
