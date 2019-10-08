from import_export import resources
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget

from .models import (Staffs, Clients, Email, PaypalEmail,
                     WebsiteUrl, TrainingUrl, TypeOfTaskRequest,
                     ChannelOfCommunications)


class StaffsResource(resources.ModelResource):

    class Meta:
        model = Staffs
        fields = (
            'username__username',
            'full_name', 'middle_name', 'phone_number',
            'SSS_number', 'TIN_number', 'pag_ibig_number',
            'philhealth', 'position', 'id_number',
            'date_of_birth', 'blood_type', 'mother_full_maiden_name', 'father_full_name',
            'emergency_contact_name', 'emergency_contact_number',
            'relationship_to_the_emergency_contact_person', 'residential_address',
            'notes', 'status', 'bank_name', 'bank_account_name',
            'bank_type', 'bank_account_number', 'base_pay',
            'hourly_rate', 'employer_share_sss', 'employer_share_ec_sss',
            'employer_share_philhealth', 'employer_share_pag_ibig',
            'total_employer', 'employee_share_sss', 'employee_share_ec_sss',
            'employee_share_philhealth', 'employee_share_pag_ibig', 'employee_tax',
            'total_employee', 'total_share_sss', 'total_share_ec_sss',
            'total_share_philhealth', 'total_share_pag_ibig', 'overall_total_share',
            'actual_date_hired', 'date_hired_in_contract', 'category',
            'email', 'maxicare_health_insurance', 'life_insurance',
            'retirement_plan', 'monthly_bonus', 'others', 'total_compensation'

        )
        export_order = (
            'username__username',
            'full_name', 'middle_name', 'phone_number',
            'SSS_number', 'TIN_number', 'pag_ibig_number',
            'philhealth', 'position', 'id_number',
            'date_of_birth', 'blood_type', 'mother_full_maiden_name', 'father_full_name',
            'emergency_contact_name', 'emergency_contact_number',
            'relationship_to_the_emergency_contact_person', 'residential_address',
            'notes', 'status', 'bank_name', 'bank_account_name',
            'bank_type', 'bank_account_number', 'base_pay',
            'hourly_rate', 'employer_share_sss', 'employer_share_ec_sss',
            'employer_share_philhealth', 'employer_share_pag_ibig',
            'total_employer', 'employee_share_sss', 'employee_share_ec_sss',
            'employee_share_philhealth', 'employee_share_pag_ibig', 'employee_tax',
            'total_employee', 'total_share_sss', 'total_share_ec_sss',
            'total_share_philhealth', 'total_share_pag_ibig', 'overall_total_share',
            'actual_date_hired', 'date_hired_in_contract', 'category',
            'email', 'maxicare_health_insurance', 'life_insurance',
            'retirement_plan', 'monthly_bonus', 'others', 'total_compensation'

        )


class ClientResource(resources.ModelResource):
    email = Field(attribute='email', widget=ManyToManyWidget(
        Email, separator=', ', field='email_address'))
    paypal_email = Field(attribute='paypal_email', widget=ManyToManyWidget(
        Email, separator=', ', field='paypal_email_address'))
    website_url = Field(attribute='website_url', widget=ManyToManyWidget(
        Email, separator=', ', field='url'))
    training_url = Field(attribute='training_url', widget=ManyToManyWidget(
        Email, separator=', ', field='url'))
    type_of_task_request = Field(attribute='type_of_task_request', widget=ManyToManyWidget(
        Email, separator=', ', field='name_of_task'))
    channel_of_communications = Field(attribute='channel_of_communications', widget=ManyToManyWidget(
        Email, separator=', ', field='name_of_channel'))

    class Meta:
        model = Clients
        fields = (
            'username__username', 'full_name', 'company_name',
            'date_signed_up', 'client_control_number', 'referred_by',
            'lead_source', 'assigned_va__name', 'assigned_pm__project_manager',
            'task_enroute', 'type_of_task', 'internal_folder_link_1',
            'internal_folder_link_2', 'internal_folder_link_3',
            'phone_number', 'company_category', 'status',
            'email', 'paypal_email',
            'website_url', 'training_url', 'type_of_task_request',
            'channel_of_communications'
        )

        export_order = (
            'username__username', 'full_name', 'company_name',
            'date_signed_up', 'client_control_number', 'referred_by',
            'lead_source', 'assigned_va__name', 'assigned_pm__project_manager',
            'task_enroute', 'type_of_task', 'internal_folder_link_1',
            'internal_folder_link_2', 'internal_folder_link_3',
            'phone_number', 'company_category', 'status',
            'email', 'paypal_email',
            'website_url', 'training_url', 'type_of_task_request',
            'channel_of_communications'
        )
