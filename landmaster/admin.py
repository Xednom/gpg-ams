from django.contrib import admin

from .models import DueDiligence, DueDiligencesCleared


class DueDiligenceProfile(admin.ModelAdmin):
    list_display = ('date_requested', 'date_completed', 'company_name',
                    'company_owner_or_requestor', 'due_date', 'project_manager',
                    'dd_team_assigned_va', 'status_of_dd')
    search_fields = ('company_name__name', 'company_owner')
    fieldsets = (
        ('Due Diligence client Information', {
            'fields': (
                'date_requested',
                'due_date',
                'company_name',
                'company_owner_or_requestor',
                'customer_care_specialist',
            )
        }),
        ("Land Data information", {
            'fields': (
                'owner_name',
                'parcel_number',
                'account_number',
                'property_address',
                'county',
                'lot_number',
                'legal_description',
                'parcel_size',
                'gps_coordinates',
                'gps_coordinates_4_corners',
                'google_map_link',
                'elevation',
                'assessed_value',
                'access_to_property',
            )
        }),
        ("Additional Land Info", {
            'fields': (
                'closest_major_city',
                'closest_small_town',
                'nearby_attractions',
            )
        }),
        ("County Data", {
            'fields': (
                'assessor_website',
                'treasurer_website',
                'recorder_clerk_website',
                'zoning_department_website',
                'gis_website',
                'cad_website',
                'planning_department_contact',
                'recorder_clerk_contact',
                'tax_office_contact',
                'assessors_office_contact',
            )
        }),
        ("Tax Data", {
            'fields': (
                'back_taxes',
                'tax_liens',
                'annual_property_taxes',
                'is_property_part_of_an_hoa',
                'how_much_dues',
            )
        }),
        ("Zoning Data", {
            'fields': (
                'zoning',
                'terrian_type',
                'property_use_code',
                'what_can_be_built',
                'time_limit_to_build',
                'can_camp',
                'notes_on_camping',
                'rv_allowed',
                'note_on_rv',
                'mobile_homes',
                'notes_on_mobile_homes',
                'is_property_flood_zone_area',
            )
        }),
        ("Data on Utilities", {
            'fields': (
                'water',
                'sewer_or_septic',
                'power',
                'gas',
                'waste',
            )
        }),
        ("Notes", {
            'fields': (
                'date_completed',
                'notes_from_the_client',
                'notes_from_the_quality_specialist',
                'notes_from_the_virtual_assistant',
                'dd_team_assigned_va',
                'project_manager',
                'status_of_dd',
            )
        }),
        ("Other information", {
            'fields': (
                'total_minutes_hours_duration',
                'attachments',
            )
        }),
    )


class DueDiligenceClearedProfile(admin.ModelAdmin):
    list_display = ('date_of_call', 'client_full_name', 'client_company_name', 'apn',
                    'call_in', 'call_out', 'total_hours', 'customer_service_representative')
    list_filter = ['client_full_name', 'client_company_name',
                   'customer_service_representative__name']
    search_fields = ('client_full_name', 'client_company_name',
                     'customer_service_representative__name')
    readonly_fields = ['total_hours']
    fieldsets = (
        ('Due Diligence Cleared Information', {
            'fields': (
                'date_of_call',
                'client_full_name',
                'client_company_name',
                'apn',
                'call_in',
                'call_out',
                'total_hours',
                'department_calling_about',
                'contact_number',
                'operators_details',
                'notes',
                'customer_service_representative'
            )
        }),
    )


admin.site.register(DueDiligence, DueDiligenceProfile)
admin.site.register(DueDiligencesCleared, DueDiligenceClearedProfile)
