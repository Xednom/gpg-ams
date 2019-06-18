from django.contrib import admin

from .models import MasterBoard

# Register your models here.
class MasterBoardProfile(admin.ModelAdmin):
    list_display = ('date_started', 'client_name', 'company_name', 'type_of_plan',
                'type_of_crm', 'type_of_voip')
    list_filter = ('type_of_plan', 'type_of_crm', 'type_of_voip', 'company_name')
    search_fields = ('client_name__full_name', 'company_name')
    fieldsets = (
        ("CallMe Master Board Informations", {
            'fields': (
                'date_started',
                'type_of_plan',
                'type_of_crm',
                'type_of_voip',
                'client_name',
                'company_name',
                'url_buyer',
                'url_seller',
                'url_property_management',
                'voicemail',
                'general_calls'
            )
        }),
    )


admin.site.register(MasterBoard, MasterBoardProfile)
