from django.contrib import admin

from .models import LandAcademyInventory, O20SmartPricing


class InventoryProfile(admin.ModelAdmin):
    list_display = ('invoice', 'date_completed',
                    'date_paid', 'project_status', 'payment_status')
    list_filter = ('project_status', 'payment_status')
    search_fields = ('invoice', 'pivot_table')
    fieldsets = (
        ("Land Academy Inventory Records", {
            'fields': (
                'date_completed',
                'date_paid',
                'invoice',
                'pivot_table',
                'project_status',
                'payment_status',
                'notes'
            )
        }),
    )


class SmartPricingProfile(admin.ModelAdmin):
    list_display = ('quality_specialist', 'date_encoded',
                    'situs_address', 'encoder', 'quality_check_status')
    list_filter = ('quality_specialist', 'date_encoded',
                   'quality_check_status')
    search_fields = ('situs_address', 'quality_specialist')
    fieldsets = (
        ("Land Academy O20 Smart Pricing Records", {
            'fields': (
                'quality_specialist',
                'situs_address',
                'trulia',
                'zillow',
                'redfin',
                'realfor',
                'realtytrac',
                'encoder',
                'date_encoded',
                'quality_check_status',
                'notes'
            )
        }),
    )


admin.site.register(LandAcademyInventory, InventoryProfile)
admin.site.register(O20SmartPricing, SmartPricingProfile)