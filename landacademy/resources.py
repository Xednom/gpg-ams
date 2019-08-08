from import_export import resources
from import_export.fields import Field

from .models import LandAcademyInventory, O20SmartPricing


class LandAcademyInventoryResource(resources.ModelResource):

    class Meta:
        model = LandAcademyInventory
        fields = (
            'date_requested', 'date_completed',
            'date_payment_made', 'order_name', 'client_la_requestor',
            'complete_order', 'status_of_order', 'payment_status',
            'invoice', 'total_items_charge', 'total_pp_fee',
            'total_charge', 'total_items_requested', 'notes'
        )
        export_order = (
            'date_requested', 'date_completed',
            'date_payment_made', 'order_name', 'client_la_requestor',
            'complete_order', 'status_of_order', 'payment_status',
            'invoice', 'total_items_charge', 'total_pp_fee',
            'total_charge', 'total_items_requested', 'notes'
        )


class O20SmartPricingResource(resources.ModelResource):

    class Meta:
        model = O20SmartPricing
        fields = (
            'date_requested', 'date_research',
            'date_encoded', 'situs_address', 'trulia',
            'zillow', 'redfin', 'realfor',
            'realtytrac', 'order_name', 'requestor_full_name',
            'researcher_name__full_name', 'quality_check_status', 
            'quality_specialist', 'notes_from_researcher', 'notes_from_qa'
        )
        export_order = (
            'date_requested', 'date_research',
            'date_encoded', 'situs_address', 'trulia',
            'zillow', 'redfin', 'realfor',
            'realtytrac', 'order_name', 'requestor_full_name',
            'researcher_name__full_name', 'quality_check_status',
            'quality_specialist', 'notes_from_researcher', 'notes_from_qa'
        )
