from django.contrib import admin
from .models import JobRequest


class JobRequestProfile(admin.ModelAdmin):
    list_display = ['date_requested', 'category', 'company_name', 'job_request_title',
                    'assigned_project_managers', 'project_status']
    list_filter = ['project_status']
    list_per_page = 15
    # change_list_template = 'jobrequest/change_list_graph.html'
    search_fields = (
        'company_name', 'company_name', 'assigned_project_managers__project_manager')
    fieldsets = (
        (None, {
            'fields': ('date_requested', 'month', 'time_in', 'time_out', 'total_minutes_hours')
        }),
        ('Job Request informations', {
            'fields': (
                'category',
                'requestors_name',
                'company_name',
                'job_request_number',
                'job_request_title',
                'job_request_instruction',
                'assigned_project_managers',
                'project_status',
                'url_training_videos',
                'assigned_va',
                'company_billable_to',
                'company_assigned_to',
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
