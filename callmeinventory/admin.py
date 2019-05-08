from django.contrib import admin
from .models import inventory


class InventoryProfile(admin.ModelAdmin):
    list_display = ('date_of_call', 'category', 'client_full_name',
                    'client_company_name', 'total_handling_time', 'total_time_transferring_leads', 'total_mins')
    list_filter = ('category',)
    search_fields = ('client_full_name', 'client_company_name')
    readonly_fields = ('total_mins',)
    fieldsets = (
        ("Call Me Inventory Informations", {
            'fields': (
                'date_of_call',
                'category',
                'client_full_name',
                'client_company_name',
                'mobile',
                'total_handling_time',
                'total_time_transferring_leads',
                'total_mins'
            )
        }),
    )

admin.site.register(inventory, InventoryProfile)
