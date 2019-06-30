from django.contrib import admin

from .models import MasterBoard

# Register your models here.
class MasterBoardProfile(admin.ModelAdmin):
    list_display = ('date_started', 'type_of_plan', 'client_name', 'company_name',   
                    'url_buyer', 'url_seller', 'url_property_management', 'voicemail',
                    'general_calls')
    list_filter = ('type_of_plan', 'type_of_crm', 'type_of_voip', 'company_name')
    search_fields = ('client_name', 'company_name')
    fieldsets = (
        ("CallMe Master Board Informations", {
            'fields': (
                'date_started',
                'type_of_plan',
                'type_of_crm',
                'type_of_voip',
                'client_name',
                'company_name',
                'email',
                'phone',
                'url_buyer',
                'url_seller',
                'url_property_management',
                'voicemail',
                'general_calls',
                'gs_integration',
                'client_folder',
                'notes'
            )
        }),
    )


admin.site.register(MasterBoard, MasterBoardProfile)
