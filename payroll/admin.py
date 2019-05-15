from django.contrib import admin
from django.db.models import Sum, Avg
from import_export.admin import ImportExportModelAdmin
from admin_totals.admin import ModelAdminTotals


from jet.filters import DateRangeFilter
from .models import VaPayroll, VaCashOut
from .resources import PayrollResource


class VaPayrollProfile(ModelAdminTotals):
    list_display = ('date', 'virtual_assistant', 'time_in', 'time_out', 'hours', 'client_name', 'salary', 'status')
    list_filter = ('date', ('date', DateRangeFilter),
                   'virtual_assistant', 'status')
    list_totals = [('salary', Sum), ('hours', Avg)]
    search_fields = ('virtual_assistant', 'client_name')
    resource_class = PayrollResource
    readonly_fields = ('salary', 'hours')
    fieldsets = (
        ("Virtual Assistant's Payroll", {
            'fields': (
                'date',
                'virtual_assistant',
                'time_in',
                'time_out',
                'hours',
                'client_name',
                'rate',
                'salary',
                'status',
                'notes'
            )
        }),
    )


class VaCashOutProfile(ModelAdminTotals):
    list_display = ('date_release', 'referrence', 'bank', 'approved_by', 'amount')
    list_filter = ('date_release', ('date_release', DateRangeFilter), 'name')
    list_totals = (['amount', Sum],)
    search_fields = ('name__virtual_assistant', 'bank', 'referrence')
    fieldsets = (
        ("Cash Out Information", {
            'fields': (
                'name',
                'date_release',
                'amount',
                'purpose',
                'referrence',
                'bank',
                'approved_by',
                'notes'
            )
        }),
    )


admin.site.register(VaPayroll, VaPayrollProfile)
admin.site.register(VaCashOut, VaCashOutProfile)
