from django.contrib import admin
from .models import inventory


class InventoryProfile(admin.ModelAdmin):
    list_display = ('type_of_form', 'client_full_name',
                    'client_company_name', 'call_duration', 'total_time_transferring_leads', 'total_mins')
    list_filter = ('type_of_form',)
    search_fields = ('client_full_name', 'client_company_name', 'customer_representative')
    readonly_fields = ('total_mins',)
    fieldsets = (
        ("Call Me Inventory Informations", {
            'fields': (
                'transferred_date',
                'date_lead_received',
                'type_of_form',
                'client_full_name',
                'client_company_name',
                'full_name_of_lead',
                'phone_number',
                'email',
                'customer_representative',
                'status',
                'financial_status',
                'call_duration',
                'total_time_transferring_leads',
                'total_mins',
                'notes'
            )
        }),
    )

admin.site.register(inventory, InventoryProfile)
