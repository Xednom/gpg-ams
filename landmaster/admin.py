from django.contrib import admin

from .models import DueDiligence, DueDiligencesCleared
from jet.filters import DateRangeFilter


class DueDiligenceProfile(admin.ModelAdmin):
    list_display = ('date_requested', 'due_date', 'company_owner_or_requestor', 
                    'company_name', 'parcel_number', 'project_manager', 'dd_va_assigned_initial_data',
                    'dd_va_assigned_call_outs_tax_data', 'dd_va_assigned_call_outs_zoning_data', 
                    'dd_va_assigned_call_outs_utilities_data', 'dd_va_assigned_call_outs_other_requests',
                    'level_of_urgency','status_initial_data', 'status_tax_data', 'status_zoning_data', 'status_utilities_data',
                    'status_other_requests', 'tax_data_completion', 'zoning_data_completion', 'utilities_data_completion',
                    'other_requests_completion', 'date_of_completion')
    list_filter = ('date_requested', 'due_date',
                   'company_owner_or_requestor', 'owner_name',
                   'status_initial_data', 'status_tax_data',
                   'status_zoning_data', 'status_utilities_data',
                   'status_other_requests', 'status_of_dd',
                   'dd_va_assigned_initial_data',
                   'dd_va_assigned_call_outs_tax_data',
                   'dd_va_assigned_call_outs_zoning_data',
                   'dd_va_assigned_call_outs_utilities_data',
                   'dd_va_assigned_call_outs_other_requests',
                   ('date_requested', DateRangeFilter))
    list_per_page = 30
    search_fields = ('company_name__name', 'company_owner')
    readonly_fields = ['total_time_allocation']
    fieldsets = (
        ('Due Diligence client Information', {
            'fields': (
                'date_requested',
                'due_date',
                'company_owner_or_requestor',
                'company_name',
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
        ("County Operator Details", {
            'fields': (
                'operator_details_tax_data',
                'operator_details_zoning_data',
                'operator_details_utilities_data',
                'operator_details_other_requests',
            )
        }),
        ("Date Of Completions", {
            'fields': (
                'initial_due_diligence_completion',
                'tax_data_completion',
                'zoning_data_completion',
                'utilities_data_completion',
                'other_requests_completion',
                'date_of_completion',
            )
        }),
        ("Notes", {
            'fields': (
                'notes_from_the_client',
                'notes_from_the_quality_specialist',
                'notes_from_the_virtual_assistant',
                'notes_on_zoning',
                'notes_on_utilities',
                'notes_on_tax',
                'additional_client_request_question',
                'additional_client_request_memo',
            )
        }),
        ("Due Diligence Statuses", {
            'fields': (
                'level_of_urgency',
                'status_initial_data',
                'status_tax_data',
                'status_zoning_data',
                'status_utilities_data',
                'status_other_requests',
                'status_of_dd',
            )
        }),
        ("Total DD Time Allocation", {
            'fields': (
                'total_hrs_for_initial_dd',
                'total_hrs_overall_dd_callouts',
                'total_time_allocation',
            )
        })
    )


class DueDiligenceClearedProfile(admin.ModelAdmin):
    list_display = ('date_of_call', 'client_full_name', 'apn',
                    'reason_of_the_call', 'total_minutes', 'customer_service_representative')
    list_filter = ['client_full_name', 'customer_service_representative']
    list_per_page = 30
    search_fields = ('client_full_name__full_name', 'customer_service_representative__full_name')
    fieldsets = (
        ('Due Diligence Cleared Information', {
            'fields': (
                'date_of_call',
                'client_full_name',
                'customer_service_representative',
                'apn',
                'total_minutes',
                'call_details',
                'department_calling_about',
                'contact_details',
                'operator_details',
                'additional_memo',
                'reason_of_the_call',
                'questions_requested_to_ask'
            )
        }),
    )


admin.site.register(DueDiligence, DueDiligenceProfile)
admin.site.register(DueDiligencesCleared, DueDiligenceClearedProfile)
