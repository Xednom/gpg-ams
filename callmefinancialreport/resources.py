from import_export import resources
from import_export.fields import Field

from .models import FinancialReport


class FinancialResource(resources.ModelResource):

    class Meta:
        model = FinancialReport
        fields = (
            'date_created', 'client_full_name__full_name',
            'client_company_name', 'date_signed_up', 'first_day_of_call',
            'first_billing_cycle', 'last_billing_cycle', 'type_of_plan',
            'total_minutes_used', 'excess_minutes', 'payment_made',
            'date_paid', 'transaction_number', 'status', 'notes_inventory',
            'notes_payment_made'
            )
