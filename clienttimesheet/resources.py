from import_export import resources
from import_export.fields import Field

from .models import TimeSheet, PaymentMade, CashOut


class TimeSheetResource(resources.ModelResource):

    class Meta:
        model = TimeSheet
        fields = (
            'company_tagging', 'shift_date', 'month_to_date',
            'clients_full_name__full_name', 'title_job_request',
            'channel_job_requested', 'job_request_description',
            'time_in', 'time_out', 'duration', 'total_items', 'additional_comments',
            'assigned_approval__full_name', 'hourly_rate_peso', 'hourly_rate_usd',
            'total_charge_peso', 'total_charge_usd', 'paypal_charge', 'total_charge_with_paypal',
            'total_amount_due', 'bonus_peso', 'bonus_given_to_company', 'others_peso',
            'others_dollars', 'status', 'admin_approval'
        )
        export_order = (
            'company_tagging', 'shift_date', 'month_to_date',
            'clients_full_name__full_name', 'title_job_request',
            'channel_job_requested', 'job_request_description',
            'time_in', 'time_out', 'duration', 'total_items', 'additional_comments',
            'assigned_approval__full_name', 'hourly_rate_peso', 'hourly_rate_usd',
            'total_charge_peso', 'total_charge_usd', 'paypal_charge', 'total_charge_with_paypal',
            'total_amount_due', 'bonus_peso', 'bonus_given_to_company', 'others_peso',
            'others_dollars', 'status', 'admin_approval'
        )


class PaymentMadeResource(resources.ModelResource):
    amount = Field()

    class Meta:
        model = PaymentMade
        fields = (
            'client_name__full_name', 'date', 'amount',
            'transaction_number', 'payment_channel', 'notes'
        )
        export_order = (
            'client_name__full_name', 'date', 'amount',
            'transaction_number', 'payment_channel', 'notes'
        )
    
    def dehydrate_amount(self, paymentmade):
        return '%s' % (paymentmade.amount)


class CashOutResource(resources.ModelResource):
    amount = Field()

    class Meta:
        model = CashOut
        fields = (
            'name__full_name', 'amount', 'reference',
            'payment_channel', 'approved_by', 'purpose',
            'notes'
        )
        export_order = (
            'name__full_name', 'amount', 'reference',
            'payment_channel', 'approved_by', 'purpose',
            'notes'
        )
    
    def dehydrate_amount(self, cashout):
        return '%s' % (cashout.amount)
    
