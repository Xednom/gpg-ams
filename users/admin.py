from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'full_name', 'email', 'date_of_birth', 'phone_number', 'position', 'id_number', 'SSS_number', 'TIN_number', 'pag_ibig_number', 'philhealth']
    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'phone_number', 'email', 'residential_address', 'date_of_birth', 'SSS_number', 'TIN_number', 'pag_ibig_number', 'philhealth', 'position', 'id_number', 'blood_type', 'mother_full_maiden_name', 'father_full_name', 'emergency_contact_name', 'emergency_contact_number', 'relationship_to_the_emergency_contact_person', 'notes', 'status')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),)


admin.site.register(CustomUser, CustomUserAdmin)
