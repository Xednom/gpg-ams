from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import CallMe


class CallMeProfile(ImportExportModelAdmin):
    list_display = ('date', 'category', 'client_name', 'company_name', 'total_handling_time',
                    'total_transferring_leads', 'total_mins')
    list_filter = ('date', 'category', 'client_name', 'company_name')
    search_fields = ('client_name', 'company_name')
    fieldsets = (
        ("Call Me Inventory Informations", {
            'fields': (
                'date',
                'category',
                'client_name',
                'company_name',
                'mobile',
                'total_handling_time',
                'total_transferring_leads',
                'total_mins'
            )
        }),
    )

admin.site.register(CallMe, CallMeProfile)