from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import VaPayroll
from .resources import PayrollResource


class VaPayrollProfile(ImportExportModelAdmin):
    list_display = ('date', 'virtual_assistant', 'time_in', 'time_out', 'hours', 'client_name', 'salary')
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
            )
        }),
    )


admin.site.register(VaPayroll, VaPayrollProfile)
