from django.contrib import admin

from .models import MasterBoard

# Register your models here.
class MasterBoardProfile(admin.ModelAdmin):
    list_display = ('status', 'date_started', 'type_of_plan', 'client_name',   
                    'email', 'phone', 'type_of_crm', 'type_of_voip')
    list_filter = ('type_of_plan', 'type_of_crm', 'type_of_voip', 'client_name')
    search_fields = ('client_name', 'url_buyer',
                     'url_seller', 'url_property_management', 
                     'general_calls', 'type_of_crm', 'type_of_voip')
    fieldsets = (
        ("CallMe Master Board Informations", {
            'fields': (
                'status',
                'date_started',
                'type_of_plan',
                'type_of_crm',
                'type_of_voip',
                'client_name',
                'email',
                'phone',
                'url_buyer',
                'url_seller',
                'url_property_management',
                'voicemail',
                'general_calls',
                'gs_integration',
                'client_folder',
                'phone_login',
                'crm_login',
                'call_forwarding_details',
                'email_form_forwarding',
                'notes'
            )
        }),
    )


admin.site.register(MasterBoard, MasterBoardProfile)
