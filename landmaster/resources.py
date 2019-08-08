from import_export import resources
from import_export.fields import Field

from .models import DueDiligence, DueDiligencesCleared


class DueDiligenceResource(resources.ModelResource):

    class Meta:
        model = DueDiligence
        fields = (
            'date_requested',
            'company_name', 'company_owner_or_requestor', 'due_date',
            'county_operator_details', 'owner_name', 'parcel_number',
            'account_number', 'property_address', 'county',
            'lot_number', 'legal_description', 'parcel_size', 'gps_coordinates',
            'gps_coordinates_4_corners', 'google_map_link',
            'elevation', 'assessed_value',
            'closest_major_city', 'closest_small_town', 'nearby_attractions', 'assessor_website',
            'treasurer_website', 'recorder_clerk_website', 'zoning_department_website',
            'gis_website', 'cad_website', 'planning_department_contact',
            'recorder_clerk_contact', 'tax_office_contact',
            'assessors_office_contact', 'utility_department_number', 'water_company_number',
            'electricity_company_number', 'propane_gas_company_number', 'natural_gas_company_number',
            'back_taxes', 'tax_liens', 'annual_property_taxes',
            'is_property_part_of_an_hoa', 'how_much_dues', 'zoning',
            'terrian_type', 'property_use_code', 'what_can_be_built',
            'time_limit_to_build', 'can_camp', 'notes_on_camping',
            'rv_allowed', 'note_on_rv', 'mobile_homes', 'notes_on_mobile_homes',
            'is_property_flood_zone_area', 'access_to_property', 'water',
            'sewer_or_septic', 'power', 'gas', 'waste', 'notes_from_the_client',
            'notes_from_the_quality_specialist', 'notes_from_the_virtual_assistant',
            'notes_on_zoning', 'notes_on_utilities', 'notes_on_tax', 
            'dd_va_assigned_initial_data', 'dd_va_assigned_call_outs_tax_data',
            'dd_va_assigned_call_outs_zoning_data', 'dd_va_assigned_call_outs_utilities_data',
            'dd_va_assigned_call_outs_other_requests', 'project_manager__full_name',
            'total_minutes_hours_duration', 'attachments', 
            'initial_due_diligence_completion', 'tax_data_completion',
            'zoning_data_completion', 'utilities_data_completion', 
            'other_requests_completion', 'date_of_completion', 'operator_details_tax_data',
            'operator_details_zoning_data', 'operator_details_utilities_data', 
            'operator_details_other_requests', 'status_initial_data', 'status_tax_data',
            'status_zoning_data', 'status_utilities_data', 'status_other_requests',
            'status_of_dd', 'level_of_urgency', 'additional_client_request_question',
            'additional_client_request_memo', 'total_hrs_for_initial_dd', 
            'total_hrs_overall_dd_callouts', 'total_time_allocation'
        )
        export_order = (
            'date_requested',
            'company_name', 'company_owner_or_requestor', 'due_date',
            'county_operator_details', 'owner_name', 'parcel_number',
            'account_number', 'property_address', 'county',
            'lot_number', 'legal_description', 'parcel_size', 'gps_coordinates',
            'gps_coordinates_4_corners', 'google_map_link',
            'elevation', 'assessed_value',
            'closest_major_city', 'closest_small_town', 'nearby_attractions', 'assessor_website',
            'treasurer_website', 'recorder_clerk_website', 'zoning_department_website',
            'gis_website', 'cad_website', 'planning_department_contact',
            'recorder_clerk_contact', 'tax_office_contact',
            'assessors_office_contact', 'utility_department_number', 'water_company_number',
            'electricity_company_number', 'propane_gas_company_number', 'natural_gas_company_number',
            'back_taxes', 'tax_liens', 'annual_property_taxes',
            'is_property_part_of_an_hoa', 'how_much_dues', 'zoning',
            'terrian_type', 'property_use_code', 'what_can_be_built',
            'time_limit_to_build', 'can_camp', 'notes_on_camping',
            'rv_allowed', 'note_on_rv', 'mobile_homes', 'notes_on_mobile_homes',
            'is_property_flood_zone_area', 'access_to_property', 'water',
            'sewer_or_septic', 'power', 'gas', 'waste', 'notes_from_the_client',
            'notes_from_the_quality_specialist', 'notes_from_the_virtual_assistant',
            'notes_on_zoning', 'notes_on_utilities', 'notes_on_tax',
            'dd_va_assigned_initial_data', 'dd_va_assigned_call_outs_tax_data',
            'dd_va_assigned_call_outs_zoning_data', 'dd_va_assigned_call_outs_utilities_data',
            'dd_va_assigned_call_outs_other_requests', 'project_manager__full_name',
            'total_minutes_hours_duration', 'attachments',
            'initial_due_diligence_completion', 'tax_data_completion',
            'zoning_data_completion', 'utilities_data_completion',
            'other_requests_completion', 'date_of_completion', 'operator_details_tax_data',
            'operator_details_zoning_data', 'operator_details_utilities_data',
            'operator_details_other_requests', 'status_initial_data', 'status_tax_data',
            'status_zoning_data', 'status_utilities_data', 'status_other_requests',
            'status_of_dd', 'level_of_urgency', 'additional_client_request_question',
            'additional_client_request_memo', 'total_hrs_for_initial_dd',
            'total_hrs_overall_dd_callouts', 'total_time_allocation'
        )


class CallOutResource(resources.ModelResource):

    class Meta:
        model = DueDiligencesCleared
        fields = (
            'date_of_call',
            'client_full_name__full_name', 'apn', 'total_minutes',
            'call_details', 'department_calling_about', 'contact_details',
            'operator_details', 'additional_memo', 'customer_service_representative__full_name',
            'customer_representative_note', 'reason_of_the_call', 'questions_requested_to_ask'
        )
        export_order = (
            'date_of_call',
            'client_full_name__full_name', 'apn', 'total_minutes',
            'call_details', 'department_calling_about', 'contact_details',
            'operator_details', 'additional_memo', 'customer_service_representative__full_name',
            'customer_representative_note', 'reason_of_the_call', 'questions_requested_to_ask'
        )
