from django.contrib import admin

from .models import DueDiligence, DueDiligencesCleared
from jet.filters import DateRangeFilter


class DueDiligenceProfile(admin.ModelAdmin):
    list_display = ('date_requested', 'date_completed', 'company_name',
                    'company_owner_or_requestor', 'due_date', 'project_manager',
                    'status_of_dd', 'total_duration')
    list_filter = ('date_requested', 'due_date',
                   'company_owner_or_requestor', 'owner_name',
                   ('date_requested', DateRangeFilter))
    search_fields = ('company_name__name', 'company_owner')
    readonly_fields = ('date_completed_initial_dd_total_time',
                       'date_completed_tax_data_total_time',
                       'date_completed_zoning_data_total_time',
                       'date_completed_utilities_total_time',
                       'date_completed_other_requests_total_time',
                       'total_duration')
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
        ("DD Team member assigned", {
            'fields': (
                'project_manager',
                'dd_va_assigned_initial_data',
                'dd_va_assigned_call_outs_tax_data',
                'dd_va_assigned_call_outs_zoning_data',
                'dd_va_assigned_call_outs_utilities_data',
                'dd_va_assigned_call_outs_other_requests',
            )
        }),
        ("Notes", {
            'fields': (
                'date_completed',
                'status_of_dd',
                'notes_from_the_client',
                'notes_from_the_quality_specialist',
                'notes_from_the_virtual_assistant',
                'notes_on_zoning',
                'notes_on_utilities',
                'notes_on_tax',
                'notes_on_legal_description',
                'notes_on_deeds',
            )
        }),
        ("Other information", {
            'fields': (
                'date_completed_initial_dd_time_in',
                'date_completed_initial_dd_time_out',
                'date_completed_initial_dd_total_time',
                'date_completed_tax_data_time_in',
                'date_completed_tax_data_time_out',
                'date_completed_tax_data_total_time',
                'date_completed_zoning_data_time_in',
                'date_completed_zoning_data_time_out',
                'date_completed_zoning_data_total_time',
                'date_completed_utilities_time_in',
                'date_completed_utilities_time_out',
                'date_completed_utilities_total_time',
                'date_completed_other_requests_time_in',
                'date_completed_other_requests_time_out',
                'date_completed_other_requests_total_time',
                'total_duration'
            )
        }),
    )


class DueDiligenceClearedProfile(admin.ModelAdmin):
    list_display = ('date_of_call', 'client_full_name', 'client_company_name', 'apn',
                    'call_in', 'call_out', 'total_hours', 'customer_service_representative')
    list_filter = ['client_full_name', 'client_company_name',
                   'customer_service_representative']
    search_fields = ('client_full_name', 'client_company_name',
                     'customer_service_representative')
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
