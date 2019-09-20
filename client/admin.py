from django.contrib import admin
from jet.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import Client, ClientLeadSource



class LeadSourceProfile(ImportExportModelAdmin):
    list_display = ('date_lead_received', 'client',
                    'lead_source', 'full_name_of_lead', 'phone_number',
                    'email', 'type_of_lead', 'lead_profile_url', 'lead_profile_under',
                    'lead_status', 'virtual_assistant')
    list_filter = ('date_lead_received', 'client', 'lead_status',
                   'virtual_assistant', 'type_of_lead', 'full_name_of_lead',
                   ('date_lead_received', DateRangeFilter))
    search_fields = ('client__full_name',
                     'virtual_assistant__full_name', 'type_of_lead', 'full_name_of_lead',
                     'lead_status')
    fieldsets = (
        ("Client Lead Source Inventory Informations", {
            'fields': (
                'date_lead_received',
                'client',
                'virtual_assistant',
                'lead_source',
                'others',
                'full_name_of_lead',
                'phone_number',
                'email',
                'type_of_lead',
                'lead_profile_url',
                'lead_profile_under',
                'lead_status',
                'notes_from_client',
                'additional_notes',
            )
        }),
    )


admin.site.register(ClientLeadSource, LeadSourceProfile)
