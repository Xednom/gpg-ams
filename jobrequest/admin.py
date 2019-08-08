from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import JobRequest, JobRequestTimeSheet
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .resources import JobRequestResource

class JobRequestProfile(ImportExportModelAdmin):
    list_display = ['date_requested', 'category', 'company_name', 'job_request_title',
                    'assigned_project_managers', 'project_status']
    list_filter = ['project_status', 'due_date', 'month',
                   'category', 'requestors_name', 'company_name',
                   'assigned_project_managers', 'assigned_va',
                   'company_tagging',
                   ('due_date', DateRangeFilter),
                   ('date_requested', DateRangeFilter)]
    list_per_page = 30
    resource_class = JobRequestResource
    search_fields = (
        'requestors_name', 'company_name', 'assigned_project_managers__project_manager', 'project_status',
        'url_training_videos', 'assigned_va')
    fieldsets = (
        ('Date Informations', {
            'fields': (
                'date_requested', 
                'due_date', 
                'month',
                )
        }),
        ('Job Request informations', {
            'fields': (
                'category',
                'requestors_name',
                'company_name',
                'job_request_title',
                'job_request_instruction',
                'assigned_project_managers',
                'project_status',
                'url_training_videos',
                'assigned_va',
                'company_tagging',
                'authorized_minutes_hours_allocation',
                )
        }),
        ("Notes", {
            'fields': (
                'additional_comments_or_feedbacks',
                'client_notes',
                'manager_notes',
                'va_notes',
            )
        })
    )


admin.site.register(JobRequest, JobRequestProfile)
