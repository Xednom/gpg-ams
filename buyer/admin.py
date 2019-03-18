from django.contrib import admin

from .models import CustomerCareSpecialist, CygnusInvestment


class CygnusInvestmentProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 
                    'provided_contact_information', 'address_of_property',
                    'name', 'agent', 'listing')
    list_filter = ('customer_care_specialist',)
    search_fields = ('customer_care_speialist__name', 'agent')
    fieldsets = (
        ('Buyer form informations', {
            'fields': (
                'call_date',
                'customer_care_specialist',
                'provided_contact_information',
                'address_of_property',
                'name',
                'agent',
                'listing',
                'phone_number',
                'email',
                'handling_time',
                'additional_notes',
            )
        }),
    )

admin.site.register(CustomerCareSpecialist)
admin.site.register(CygnusInvestment, CygnusInvestmentProfile)
