from django.contrib import admin
from django.forms import modelformset_factory
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from .models import ClientName, CallDetails


class ClientNameAdminForm(BaseDynamicEntityForm):
    model = ClientName


class ClientNameAdmin(BaseEntityAdmin):
    form = ClientNameAdminForm


class CallDetailsAdminForm(BaseDynamicEntityForm):
    model = CallDetails


class CallDetailsAdmin(BaseEntityAdmin):
    form = CallDetailsAdminForm


class CallDetailsInline(admin.StackedInline):
    """
    Inline form for Client call informations
    """
    model = CallDetails
    config_formset = modelformset_factory(ClientName, fields=('__all__'))
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        """                                                                                    
        Limit the types of configuration items you can add.                                    
        """
        field = super(CallDetailsInline, self). \
            formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'client_name':
            field.queryset = field.queryset.filter(description='GPG')


class ClientNameProfile(admin.ModelAdmin):
    inlines = [CallDetailsInline]
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)
    list_per_page = 15
    search_fields = ('name',)
    fieldsets = (
        ('Client Information', {
            'fields': (
                'name',
                'description',
                'is_active',
            )
        }),
    )


class CallDetailsProfile(admin.ModelAdmin):
    list_display = ('client_name', 'letter_info',)
    list_filter = ('client_name',)
    list_per_page = 15
    search_fields = ('client_name__name',)
    fieldsets = (
        ('Call Information', {
            'fields': (
                'client_name',
                'letter_info',
            )
        }),
    )


admin.site.register(ClientName, ClientNameProfile)
admin.site.register(CallDetails, CallDetailsProfile)
# admin.site.register(CallDetails, CallDetailsAdmin)
