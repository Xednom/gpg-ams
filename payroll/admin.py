from django.contrib import admin

from .models import VaPayroll


class VaPayrollProfile(admin.ModelAdmin):
    list_display = ('date', 'virtual_assistant', 'time_in', 'time_out', 'client_name', 'salary')
    search_fields = ('virtual_assistant', 'client_name')
    readonly_fields = ('salary',)
    fieldsets = (
        ("Virtual Assistant's Payroll", {
            'fields': (
                'date',
                'virtual_assistant',
                'time_in',
                'time_out',
                'client_name',
                'rate',
                'salary',
            )
        }),
    )


admin.site.register(VaPayroll, VaPayrollProfile)