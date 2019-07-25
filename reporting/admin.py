from django.contrib import admin
from .models import (
    DateInformation,
    Task,
    VATimeSheet
)


# class VATimeSheetProfile(admin.ModelAdmin):
#     list_display = [
#         'shift_date',
#         'clients_full_name',
#         'title_of_job_request',
#         'title_of_job_request',
#         'time_in',
#         'time_out',
#         'assigned_job_request_from'
#     ]
#     list_filters = ('date_information', 'month_to_date')
#     list_per_page = 15
#     search_fields = ('clients_full_name', 'list_of_task')
#     fieldsets = (
#         ('Date information', {
#             'fields': ('shift_date', 'month_to_date', 'date_information')
#         }),
#         ('Client job information', {
#             'fields': ('clients_full_name', 'title_of_job_request', 'list_of_task', 'job_request_description',)
#         }),
#         ('Time allocated', {
#             'fields': ('time_in', 'time_out', 'duration', 'hourly_rate')
#         }),
#         ('Other informations', {
#             'fields': ('additional_comments', 'assigned_job_request_from', 'project_manager', 'approval_from_project_manager', 'approval_of_admin')
#         })
#     )


# class DateInformationProfile(admin.ModelAdmin):
#     fieldsets = (
#         ('Work week durations', {
#             'fields': ('weeks',)
#         }),
#     )


# class TaskProfile(admin.ModelAdmin):
#     fieldsets = (
#         ('Job information', {
#             'fields': ('job_name',)
#         }),
#     )


# class ClientNameProfile(admin.ModelAdmin):
#     fieldsets = (
#         ('Client information', {
#             'fields': ('name',)
#         }),
#     )


# admin.site.register(DateInformation, DateInformationProfile)
# admin.site.register(Task, TaskProfile)
# admin.site.register(VATimeSheet, VATimeSheetProfile)
