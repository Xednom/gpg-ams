from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import LandAcademyInventory, O20SmartPricing
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .resources import LandAcademyInventoryResource, O20SmartPricingResource


class InventoryProfile(ImportExportModelAdmin):
    list_display = ('invoice', 'date_requested', 'order_name', 'total_items_requested', 'total_items_charge',
                    'total_pp_fee', 'total_charge', 'client_la_requestor', 'date_completed', 'status_of_order', 'payment_status')
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
                'client_la_requestor',
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
    list_display = ('date_requested', 'quality_specialist', 'date_encoded',
                    'situs_address', 'quality_check_status')
    list_filter = ('quality_specialist', 'date_encoded',
                   'quality_check_status', 'date_requested',
                   'order_name', 'researcher_name', 'quality_check_status',
                   ('date_requested', DateRangeFilter))
    list_per_page = 30
    readonly_fields = ['date_encoded']
    search_fields = ('situs_address', 'quality_specialist')
    resource_class = O20SmartPricingResource
    fieldsets = (
        ("Land Academy O20 Smart Pricing Records", {
            'fields': (
                'date_requested',
                'situs_address',
                'trulia',
                'zillow',
                'redfin',
                'realfor',
                'realtytrac',
                'order_name',
                'date_research',
                'researcher_name',
                'quality_specialist',
                'quality_check_status',
                'date_encoded',
                'notes_from_researcher',
                'notes_from_qa',
            )
        }),
    )


admin.site.register(LandAcademyInventory, InventoryProfile)
admin.site.register(O20SmartPricing, SmartPricingProfile)
