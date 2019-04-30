from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import VaPayroll, VaCashOut
from .resources import PayrollResource


class VaPayrollProfile(ImportExportModelAdmin):
    list_display = ('date', 'virtual_assistant', 'time_in', 'time_out', 'hours', 'client_name', 'salary', 'status')
    list_filter = ('date', 'virtual_assistant')
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


class VaCashOutProfile(ImportExportModelAdmin):
    list_display = ('date_release', 'referrence', 'bank', 'approved_by', 'amount')
    list_filter = ('date_release', 'name')
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
