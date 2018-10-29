from django.contrib import admin
from .models import (
    WeekToDate,
    ClientName,
    Job,
    Report
)


class ReportingProfile(admin.ModelAdmin):
    list_display = (
        'shift_date',
        'month_to_date',
        'week_to_date',
        'clients_full_name',
        'title_of_job_request',
        'job_requested_from',
        'job_request_description',
        'time_in',
        'time_out',
        'duration',
        'total_items_finished',
        'additional_comments',
        'assigned_job_request_to',
        'hourly_rate',
        'approval_from_project_manager',
        'approval_of_admin'
    )


admin.site.register(WeekToDate)
admin.site.register(ClientName)
admin.site.register(Job)
admin.site.register(Report, ReportingProfile)
