from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext as _

from django.forms import modelformset_factory

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
        CustomUser, 
        Staffs, 
        Clients, 
        Email, 
        PaypalEmail, 
        WebsiteUrl, 
        ClientProfiling,
        TrainingUrl,
        TypeOfTaskRequest,
        ChannelOfCommunications,
        NotesAfterTraining,
    )


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username']
    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('notes', 'is_staffs','is_client')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PaypalEmailInline(admin.TabularInline):
    model = PaypalEmail
    extra = 1


class WebsiteInline(admin.TabularInline):
    model = WebsiteUrl
    extra = 1


class TrainingUrlInline(admin.TabularInline):
    model = TrainingUrl
    extra = 1


class TypeOfTaskRequestInline(admin.TabularInline):
    model = TypeOfTaskRequest
    extra = 1


class ChanngelOfCommunicationsInline(admin.TabularInline):
    model = ChannelOfCommunications
    extra = 1

class NotesAfterTrainingInline(admin.TabularInline):
    model = NotesAfterTraining
    extra = 1


class StaffProfile(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email',
                    'phone_number', 'SSS_number',
                    'TIN_number', 'pag_ibig_number',
                    'philhealth', 'position', 'status',
                    'category')
    list_filter = ('full_name', 'position', 'status')
    search_fields = ('full_name', 'position', 'SSS_number',
                     'TIN_number', 'pag_ibig_number')
    readonly_fields = ('total_employer', 'total_employee')
    fieldsets = (
        ('Staff Informations', {
            'fields': (
                'username',
                'full_name',
                'middle_name',
                'email',
                'actual_date_hired',
                'date_hired_in_contract',
                'base_pay',
                'hourly_rate',
                'phone_number',
                'SSS_number',
                'TIN_number',
                'pag_ibig_number',
                'philhealth',
                'position',
                'id_number',
                'status',
                'category',
                'notes',
            )
        }),
        ('Personal Informations', {
            'fields': (
                'date_of_birth',
                'blood_type',
                'mother_full_maiden_name',
                'father_full_name',
                'emergency_contact_name',
                'emergency_contact_number',
                'relationship_to_the_emergency_contact_person',
                'residential_address',
            )
        }),
        ('Bank Information', {
            'fields': (
                'bank_name',
                'bank_account_name',
                'bank_type',
                'bank_account_number',
            )
        }),
        ('Employer Share', {
            'fields': (
                'employer_share_sss',
                'employer_share_ec_sss',
                'employer_share_philhealth',
                'employer_share_pag_ibig',
                'total_employer',
            )
        }),
        ('Employee Share', {
            'fields':(
                'employee_share_sss',
                'employee_share_ec_sss',
                'employee_share_philhealth',
                'employee_share_pag_ibig',
                'employee_tax',
                'total_employee',
            )
        }),
        ('Total Shares', {
            'fields': (
                'total_share_sss',
                'total_share_ec_sss',
                'total_share_philhealth',
                'total_share_pag_ibig',
                'overall_total_share',
            )
        }),
    )


class ClientProfile(admin.ModelAdmin):
    inlines = [
        EmailInline,
        PaypalEmailInline,
        WebsiteInline,
        TrainingUrlInline,
        TypeOfTaskRequestInline,
        ChanngelOfCommunicationsInline,
        NotesAfterTrainingInline,
    ]
    list_display = ('company_category', 'status', 'client_control_number', 'username', 'full_name', 'company_name',
                    'assigned_va', 'assigned_pm', 'phone_number', 'internal_folder_link_1',
                    'internal_folder_link_2', 'internal_folder_link_3')
    list_filter = ['company_name']
    search_fields = ('username__username', 'full_name', 'company_name')
    fieldsets = (
        ('Client Informations', {
            'fields': (
                'company_category',
                'status',
                'username',
                'full_name',
                'company_name',
                'phone_number',
                'client_control_number',
                'referred_by',
                'lead_source',
                'internal_folder_link_1',
                'internal_folder_link_2',
                'internal_folder_link_3',
            )
        }),
        ('GPG Employee assigned to you', {
            'fields': (
                'assigned_va',
                'assigned_pm',
            )
        }),
        ('Important Information', {
            'fields': (
                'date_signed_up',
            )
        }),
    )

# def get_queryset(self, request):
#     queryset = super(ClientProfile, self).get_queryset(request)
#     return queryset.filter(is_client=True)


class ClientProfilingInfo(admin.ModelAdmin):
    list_display = ('client_name', 'kind_of_client')
    list_filter = ('client_name', 'kind_of_client')
    search_fields = ('client_name', 'kind_of_client')
    fieldsets = (
        ('Client Profiling', {
            'fields': (
                'client_name',
                'kind_of_client',
                'notes',
            )
        }),
    )
    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Staffs, StaffProfile)
admin.site.register(Clients, ClientProfile)
admin.site.register(ClientProfiling, ClientProfilingInfo)
