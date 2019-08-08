from jet.filters import DateRangeFilter
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from admin_totals.admin import ModelAdminTotals

from django.db.models import Sum

from . models import TimeSheet, PaymentMade, CashOut


class TimeSheetProfile(ModelAdminTotals):
    list_display = ('shift_date', 'clients_full_name', 'duration',
                    'title_job_request', 'assigned_va', 'assigned_pm', 
                    'admin_approval', 'hourly_rate_peso', 'total_charge_peso', 
                    'hourly_rate_usd', 'total_amount_due')
    list_filter = ('company_tagging', 'shift_date', 'assigned_va',
                   'assigned_pm', ('shift_date', DateRangeFilter), 
                   'clients_full_name', 'month_to_date', 
                   'status', 'admin_approval')
    list_totals = [('duration', Sum), ('total_charge_peso', Sum), 
                   ('total_charge_usd', Sum), ('total_amount_due', Sum)]
    search_fields = ('company_tagging', 'clients_full_name__full_name', 
                     'channel_job_requested', 'title_job_request',
                     'assigned_va__full_name', 'assigned_pm__full_name')
    readonly_fields = ('total_amount_due', 'total_charge_peso', 
                       'total_charge_usd', 'total_charge_with_paypal', 'duration',
                       'paypal_charge')
    fieldsets = (
        ("TimeSheet General Information", {
            'fields': (
                'company_tagging',
                'shift_date',
                'month_to_date',
                'clients_full_name',
                'title_job_request',
                'channel_job_requested',
                'job_request_description',
                'total_items',
                'status',
                'admin_approval',
                'additional_comments'
            )
        }),
        ("Time logged in", {
            'fields': (
                'time_in',
                'time_out',
                'duration'
            )
        }),
        ("GPG Employee assigned", {
            'fields': (
                'assigned_va',
                'assigned_pm'
            )
        }),
        ("Amount Information", {
            'fields': (
                'hourly_rate_peso',
                'hourly_rate_usd',
                'bonus_peso',
                'bonus_given_to_company',
                'others_peso',
                'others_dollars',
                'total_charge_peso',
                'total_charge_usd',
                'paypal_charge',
                'total_charge_with_paypal',
                'total_amount_due'
            )
        }),
    )


class PaymentMadeProfile(ModelAdminTotals):
    list_display = ('date', 'client_name', 'transaction_number',
                    'payment_channel', 'amount',)
    list_filter = (('date', DateRangeFilter), 'date', 'payment_channel',
                    'client_name')
    list_totals = [('amount', Sum)]
    list_per_page = 30
    search_fields = ('transaction_number', 'payment_channel',
                     'client_name__full_name')
    fieldsets = (
        ("Payment Made for the Client", {
            'fields': (
                'date',
                'client_name',
                'amount',
                'transaction_number',
                'payment_channel',
                'notes',
            )
        }),
    )


class CashoutProfile(ModelAdminTotals):
    list_display = ('cash_date_release', 'name', 'reference',
                    'payment_channel', 'approved_by', 'purpose', 'amount',)
    list_filter = (('cash_date_release', DateRangeFilter),
                   'cash_date_release', 'payment_channel',
                   'name')
    list_totals = [('amount', Sum)]
    search_fields = ('reference', 'payment_channel',
                     'name__full_name')
    fieldsets = (
        ("Cashout made by the VA", {
            'fields': (
                'name',
                'amount',
                'cash_date_release',
                'reference',
                'payment_channel',
                'approved_by',
                'purpose',
                'notes'
            )
        }),
    )


admin.site.register(TimeSheet, TimeSheetProfile)
admin.site.register(PaymentMade, PaymentMadeProfile)
admin.site.register(CashOut, CashoutProfile)
