from django.contrib import admin

from .models import Inventory
from import_export.admin import ImportExportModelAdmin, ExportMixin


class InventoryProfile(ImportExportModelAdmin):
    list_display = ('date_requested', 'date_completed', 'apn',
                    'type_of_marketing_sites', 'client_full_name',
                    'client_company_name', 'marketing_associate', 'status')
    list_filter = ('client_full_name', 'client_company_name', 'status',
                   'post_for_approval', 'marketing_associate')
    list_per_page = 30
    search_fields = ('client_full_name', 'client_company_name', 'apn')
    fieldsets = (
        ('Date Informations', {
            'fields': (
                'date_requested',
                'date_completed',
            )
        }),
        ('Marketing Sites Informations', {
            'fields': (
                'type_of_marketing_sites',
                'indicate_others',
                'client_full_name',
                'client_company_name',
                'apn',
                'title_of_the_post',
                'description',
                'price',
                'location',
                'url_link',
                'marketing_associate',
                'duration',
                'post_for_approval',
                'status',
                'additional_notes',
                'notes_from_the_client',
            )
        })
    )

admin.site.register(Inventory, InventoryProfile)
