from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from admin_totals.admin import ModelAdminTotals

from django.db.models import Sum

from . models import TimeSheet, PaymentMade


class TimeSheetProfile(ModelAdminTotals):
    list_display = ('company_tagging', 'shift_date', 'month_to_date', 'clients_full_name',
                    'title_job_request', 'time_in', 'time_out', 'duration', 'hourly_rate',
                    'total_tax_fee', 'total_amount_due')
    list_filter = ('company_tagging', 'shift_date', 'clients_full_name')
    list_totals = [('total_tax_fee', Sum), ('total_amount_due', Sum), ('duration', Sum)]
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


class PaymentMadeProfile(ModelAdminTotals):
    list_display = ('date', 'client_name', 'reference',
                    'payment_channel', 'amount',)
    list_filter = ('date', 'reference', 'payment_channel')
    list_totals = [('amount', Sum)]
    search_fields = ('reference', 'payment_channel')
    fieldsets = (
        ("Payment Made for the Client", {
            'fields': (
                'date',
                'client_name',
                'amount',
                'reference',
                'payment_channel',
                'notes',
            )
        }),
    )

admin.site.register(TimeSheet, TimeSheetProfile)
admin.site.register(PaymentMade, PaymentMadeProfile)
