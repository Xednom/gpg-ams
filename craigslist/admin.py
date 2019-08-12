from django.contrib import admin
from jet.filters import DateRangeFilter
from .models import CraiglistInventory


class CraiglistProfile(admin.ModelAdmin):
    list_display = ('date', 'client_name_company_name', 'cl_admin_support',
                    'posted_ads', 'flagged_ads', 'sticked_ads', 'stick_rates')
    list_filter = ('client_name_company_name', 'cl_admin_support', 'date',
                   ('date', DateRangeFilter))
    list_per_page = 30
    search_fields = ('client_name_company_name__full_name', 'cl_admin_support__full_name')
    fieldsets = (
        ("Craigs List Inventory Records", {
            'fields': (
                'date',
                'client_name_company_name',
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
