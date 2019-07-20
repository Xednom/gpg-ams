from django.contrib import admin
from .models import JobRequest, JobRequestTimeSheet


class JobRequestProfile(admin.ModelAdmin):
    list_display = ['date_requested', 'category', 'company_name', 'job_request_title',
                    'assigned_project_managers', 'project_status']
    list_filter = ['project_status']
    list_per_page = 15
    # change_list_template = 'jobrequest/change_list_graph.html'
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


class JobTimeSheetProfile(admin.ModelAdmin):
    list_display = ['created_at', 'job_title', 'staff', 'time_in',
                    'time_out', 'total_minutes_hours']
    list_filter = ['job_title', 'staff']
    list_per_page = 15
    readonly_fields = ('created_at', 'updated_at', 'total_minutes_hours')
    search_fields = ('staff', 'job_title__job_title')
    fieldsets = (
        ('Time Sheet Informations', {
            'fields': (
                'staff',
                'client',
                'job_title',
                'created_at',
                'updated_at',
                'time_in',
                'time_out',
                'total_minutes_hours'
            )
        }),
    )


admin.site.register(JobRequest, JobRequestProfile)
admin.site.register(JobRequestTimeSheet, JobTimeSheetProfile)
