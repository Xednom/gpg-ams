from django.contrib import admin

from .models import CraiglistInventory


class CraiglistProfile(admin.ModelAdmin):
    list_display = ('date', 'client_company_name', 'cl_admin_support',
                    'posted_ads', 'flagged_ads', 'sticked_ads', 'stick_rates')
    list_filter = ('client_company_name', 'cl_admin_support', 'date')
    search_fields = ('client_company_name', 'cl_admin_support')
    fieldsets = (
        ("Craigs List Inventory Records", {
            'fields': (
                'date',
                'client_company_name',
                'cl_admin_support',
                'posted_ads',
                'flagged_ads',
                'sticked_ads',
                'stick_rates',
                'notes',
            )
        }),
    )

admin.site.register(CraiglistInventory, CraiglistProfile)