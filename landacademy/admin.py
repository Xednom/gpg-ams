from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import LandAcademyInventory, O20SmartPricing
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .resources import LandAcademyInventoryResource, O20SmartPricingResource


class InventoryProfile(ImportExportModelAdmin):
    list_display = ('invoice', 'date_requested', 'order_name', 'total_items_requested', 'total_items_charge',
                    'total_pp_fee', 'total_charge', 'client', 'date_completed', 'status_of_order', 'payment_status')
    list_filter = ('status_of_order', 'payment_status')
    list_per_page = 30
    search_fields = ('invoice', 'pivot_table')
    readonly_fields = ['total_items_charge', 'total_pp_fee', 'total_charge']
    resource_class = LandAcademyInventoryResource
    fieldsets = (
        ("Land Academy Inventory Records", {
            'fields': (
                'date_requested',
                'date_completed',
                'order_name',
                'total_items_requested',
                'client',
                'complete_order',
                'status_of_order',
                'invoice',
                'total_items_charge',
                'total_pp_fee',
                'total_charge',
                'payment_status',
                'date_payment_made',
                'notes'
            )
        }),
    )


class SmartPricingProfile(ImportExportModelAdmin):
    list_display = ('date_completed', 'client', 'job_order',
                    'virtual_assistant')
    list_filter = ('client', 'virtual_assistant',
                   'date_completed',('date_completed', DateRangeFilter))
    list_per_page = 30
    search_fields = ('situs_address', 'virtual_assistant__full_name', 'client__full_name')
    resource_class = O20SmartPricingResource
    fieldsets = (
        ("Land Academy O20 Smart Pricing Records", {
            'fields': (
                'date_completed',
                'client',
                'virtual_assistant',
                'job_order',
                'situs_address',
                'trulia',
                'zillow',
                'redfin',
                'realfor',
                'realtytrac',
                'notes'
            )
        }),
    )


admin.site.register(LandAcademyInventory, InventoryProfile)
admin.site.register(O20SmartPricing, SmartPricingProfile)
