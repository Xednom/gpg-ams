from django.contrib import admin
from jet.filters import DateRangeFilter
from django.db.models import Sum, Avg
from admin_totals.admin import ModelAdminTotals
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import FinancialReport
from .resources import FinancialResource

class FinancialReportProfile(ImportExportModelAdmin):
    list_display = ('date_signed_up', 'client_full_name',
                    'client_company_name', 
                    'first_day_of_call', 'first_billing_cycle', 
                    'last_billing_cycle', 'status', 'type_of_plan',
                    'total_minutes_used', 'excess_minutes', 'payment_made',
                    'date_paid')
    list_filter = ('date_signed_up', 'client_full_name__full_name',
                   'client_company_name', 'date_paid', 'status',
                   ('first_day_of_call', DateRangeFilter),
                   ('first_billing_cycle', DateRangeFilter),
                   ('last_billing_cycle', DateRangeFilter),
                   ('date_paid', DateRangeFilter))
    list_totals = [('type_of_plan', Sum), ('payment_made', Sum),
                   ('total_minutes_used', Sum), ('excess_minutes', Sum)]
    search_fields = ('client_full_name__full_name', 'client_company_name',
                    'transaction_number')
    readonly_fields = ('excess_minutes',)
    resource_class = FinancialResource
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
                'payment_made',
                'date_paid',
                'transaction_number',
                'status',
                'notes_payment_made',
            )
        }),
        ('CallMe Minutes Inventory', {
            'fields': (
                'type_of_plan',
                'total_minutes_used',
                'excess_minutes',
                'notes_inventory',
            )
        })
    )

admin.site.register(FinancialReport, FinancialReportProfile)
