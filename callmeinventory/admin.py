from django.contrib import admin
from jet.filters import DateRangeFilter
from django.db.models import Sum, Avg

from admin_totals.admin import ModelAdminTotals
from import_export.admin import ImportExportModelAdmin, ExportMixin


from .models import inventory, VaForm


class InventoryProfile(ImportExportModelAdmin):
    list_display = ('date_lead_received', 'type_of_form',
                    'client_full_name', 'full_name_of_lead', 
                    'phone_number', 'status', 'lead_conversion', 'financial_status',
                    'call_duration', 'total_time_transferring_leads', 'total_mins')
    list_filter = ('type_of_form', 'status', 'financial_status', 
                   'client_full_name', 'lead_conversion',
                   ('transferred_date', DateRangeFilter),
                   ('date_lead_received', DateRangeFilter))
    list_totals = [('call_duration', Sum), ('total_time_transferring_leads', Sum),
                   ('total_mins', Sum)]
    search_fields = ('client_full_name',
                     'customer_representative', 'type_of_form', 'status', 
                     'financial_status')
    readonly_fields = ('total_mins',)
    fieldsets = (
        ("Call Me Inventory Informations", {
            'fields': (
                'date_lead_received',
                'type_of_form',
                'client_full_name',
                'full_name_of_lead',
                'phone_number',
                'email',
                'lead_conversion',
                'customer_representative',
                'lead_transferred_by',
                'transferred_date',
                'status',
                'financial_status',
                'call_duration',
                'total_time_transferring_leads',
                'total_mins',
                'notes',
            )
        }),
    )


class VaFormProfile(ImportExportModelAdmin):
    list_display = ('client_full_name', 'type_of_script',
                    'client_call_forwarding_number', 'company_call_forwarding_number',
                    'created_at', 'updated_at')
    list_filter = ('client_full_name', 'type_of_script',
                   ('created_at', DateRangeFilter),
                   ('updated_at', DateRangeFilter))
    search_fields = ('client_full_name__full_name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Call Me Forms Information", {
            'fields': (
                'client_full_name',
                'type_of_script',
                'script_link',
                'gs_integration',
                'client_call_forwarding_number',
                'company_call_forwarding_number',
                'notes'
            )
        }),
    )

admin.site.register(inventory, InventoryProfile)
admin.site.register(VaForm, VaFormProfile)