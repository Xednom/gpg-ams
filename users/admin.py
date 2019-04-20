from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext as _

from django.forms import modelformset_factory

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Staffs, Clients, Email, PaypalEmail, WebsiteUrl


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username']
    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','notes', 'is_staffs','is_client')}),
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


class StaffProfile(admin.ModelAdmin):
    list_display = ('username', 'full_name',
                    'phone_number', 'SSS_number',
                    'TIN_number', 'pag_ibig_number',
                    'philhealth', 'position', 'status')
    list_filter = ('full_name', 'position', 'status')
    search_fields = ('full_name', 'position', 'SSS_number',
                     'TIN_number', 'pag_ibig_number')
    fieldsets = (
        ('Staff Informations', {
            'fields': (
                'username',
                'full_name',
                'phone_number',
                'SSS_number',
                'TIN_number',
                'pag_ibig_number',
                'philhealth',
                'position',
                'id_number',
                'status',
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
    )


class ClientProfile(admin.ModelAdmin):
    inlines = [
        EmailInline,
        PaypalEmailInline,
        WebsiteInline,
    ]
    list_display = ('username','full_name', 'company_name')
    list_filter = ['company_name']
    readonly_fields = ['date_signed_up']
    search_fields = ('username', 'full_name', 'company_name')
    fieldsets = (
        ('Client Informations', {
            'fields': (
                'username',
                'full_name',
                'company_name',
                'client_control_number',
                'referral',
            )
        }),
        ('Important Information', {
            'fields': (
                'date_signed_up',
            )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Staffs, StaffProfile)
admin.site.register(Clients, ClientProfile)
