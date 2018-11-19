from django.contrib import admin
from .models import (
    WeekToDate,
    Job,
    Report
)


class ReportingProfile(admin.ModelAdmin):
    list_display = [
        'shift_date',
        'clients_full_name',
        'title_of_job_request',
        'title_of_job_request',
        'time_in',
        'time_out',
        'assigned_job_request_to'
    ]
    list_filters = ('week_to_date', 'month_to_date')
    list_per_page = 15
    search_fields = ('clients_full_name', 'job_requested_from')
    fieldsets = (
        ('Date information', {
            'fields': ('shift_date', 'month_to_date', 'week_to_date')
        }),
        ('Client job information', {
            'fields': ('clients_full_name', 'title_of_job_request', 'job_requested_from', 'job_request_description',)
        }),
        ('Time allocated', {
            'fields': ('time_in', 'time_out', 'duration', 'hourly_rate')
        }),
        ('Other informations', {
            'fields': ('additional_comments', 'assigned_job_request_to', 'project_manager', 'approval_from_project_manager', 'approval_of_admin')
        })
    )


class WeekToDateProfile(admin.ModelAdmin):
    fieldsets = (
        ('Work week durations', {
            'fields': ('weeks',)
        }),
    )


class JobProfile(admin.ModelAdmin):
    fieldsets = (
        ('Job information', {
            'fields': ('job_name',)
        }),
    )


class ClientNameProfile(admin.ModelAdmin):
    fieldsets = (
        ('Client information', {
            'fields': ('name',)
        }),
    )


admin.site.register(WeekToDate, WeekToDateProfile)
admin.site.register(Job, JobProfile)
admin.site.register(Report, ReportingProfile)
