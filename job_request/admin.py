from django.contrib import admin
from .models import JobRequest


class JobRequestProfile(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('date', 'due_date', 'total_hours_minutes_allocated')
        }),
        ('Job Request informations', {
            'fields': (
            'client_code',
            'job_request_title',
            'job_request_sent_via',
            'job_request_instruction',
            'project_manager',
            'VA_admin_support',
            'status_of_the_job_request',
            'notes_and_coaching_from_project_manager'
           )
        }),
    )
