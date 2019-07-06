from django.contrib import admin
from jet.filters import DateRangeFilter
from django.db.models import Sum, Avg
from admin_totals.admin import ModelAdminTotals

from .models import FinancialReport


class FinancialReportProfile(ModelAdminTotals):
    list_display = ('date_signed_up', 'client_full_name',
                    'client_company_name', 'type_of_plan', 
                    'total_minutes_used', 'excess_minutes', 'payment_made', 'date_paid')
    list_filter = ('date_signed_up', 'client_full_name',
                   'client_company_name', 'date_paid', 'status',
                   ('first_day_of_call', DateRangeFilter),
                   ('first_billing_cycle', DateRangeFilter),
                   ('last_billing_cycle', DateRangeFilter),
                   ('date_paid', DateRangeFilter))
    list_totals = [('type_of_plan', Sum), ('payment_made', Sum), 
                   ('total_minutes_used', Sum), ('excess_minutes', Sum)]
    search_fields = ('client_full_name', 'client_company_name',
                    'transaction_number')
    fieldsets = (
        ('CallMe Payment Made', {
            'fields': (
                'date_created',
                'client_full_name',
                'client_company_name',
                'date_signed_up',
                'first_day_of_call',
                'first_billing_cycle',
                'last_billing_cycle',
                'type_of_plan',
                'payment_made',
                'date_paid',
                'transaction_number',
                'status',
                'notes_payment_made',
            )
        }),
        ('CallMe Minutes Inventory', {
            'fields': (
                'total_minutes_used',
                'excess_minutes',
                'notes_inventory',
            )
        })
    )


admin.site.register(FinancialReport, FinancialReportProfile)
