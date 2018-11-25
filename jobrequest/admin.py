from django.contrib import admin
from .models import JobRequest


class JobRequestProfile(admin.ModelAdmin):
    list_display = ['job_request_title', 'job_request_sent_via', 'project_managers', 'client_code', 'status']
    list_filter = ['status']
    list_per_page = 15
    search_fields = ('client_code', 'project_managers__project_manager', 'job_request_title')
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
                    'project_managers',
                    'VA_admin_support',
                    'status',
                    'notes_and_coaching_from_project_manager'
                )
        })
    )


admin.site.register(JobRequest, JobRequestProfile)
