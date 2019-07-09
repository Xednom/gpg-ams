from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import inventory


class InventoryProfile(admin.ModelAdmin):
    list_display = ('date_lead_received', 'type_of_form',
                    'client_full_name', 'client_company_name',
                    'full_name_of_lead', 'phone_number', 'status', 'financial_status',
                    'call_duration', 'total_time_transferring_leads', 'total_mins')
    list_filter = ('type_of_form', 'status', 'financial_status')
    search_fields = ('client_full_name', 'client_company_name',
                     'customer_representative', 'type_of_form', 'status', 
                     'financial_status', ('transferred_date', DateRangeFilter),
                     ('date_lead_received', DateRangeFilter))
    readonly_fields = ('total_mins',)
    fieldsets = (
        ("Call Me Inventory Informations", {
            'fields': (
                'date_lead_received',
                'type_of_form',
                'client_full_name',
                'client_company_name',
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

admin.site.register(inventory, InventoryProfile)
