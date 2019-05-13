from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . models import TimeSheet, PaymentMade


class TimeSheetProfile(ImportExportModelAdmin):
    list_display = ('company_tagging', 'shift_date', 'month_to_date', 'clients_full_name',
                    'title_job_request', 'time_in', 'time_out', 'duration', 'hourly_rate',
                    'total_tax_fee', 'total_amount_due')
    list_filter = ('company_tagging', 'shift_date', 'clients_full_name')
    search_fields = ('company_tagging', 'clients_full_name', 'shift_date', 'month_to_date',
                     'title_job_request')
    readonly_fields = ('total_tax_fee', 'total_amount_due', 'amount_charge', 'duration')
    fieldsets = (
        ("Client TimeSheet Informations", {
            'fields': (
                'company_tagging',
                'shift_date',
                'month_to_date',
                'clients_full_name',
                'title_job_request',
                'job_request',
                'time_in',
                'time_out',
                'duration',
                'total_items',
                'additional_comments',
                'assigned_job_request_to',
                'hourly_rate',
                'amount_charge',
                'tax_fee',
                'total_tax_fee',
                'total_amount_due'
            )
        }),
    )


class PaymentMadeProfile(ImportExportModelAdmin):
    list_display = ('date', 'amount', 'reference', 'payment_channel')
    list_filter = ('date', 'reference', 'payment_channel')
    search_fields = ('reference', 'payment_channel')
    fieldsets = (
        ("Payment Made for the Client", {
            'fields': (
                'date',
                'amount',
                'reference',
                'payment_channel',
                'notes',
            )
        }),
    )

admin.site.register(TimeSheet, TimeSheetProfile)
admin.site.register(PaymentMade, PaymentMadeProfile)