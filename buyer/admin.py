from django.contrib import admin

from .models import CustomerCareSpecialist, CygnusInvestment, WeBuyAcreageLlc


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

class WeBuyAcreageLlcProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist',
                    'name_of_the_caller', 'phone_number_of_caller')
    list_filter = ('customer_care_specialist',)
    search_fields = ('customer_care_specialist__name', 'are_you_an_agent')
    fieldsets = (
        ('Buyer form informations', {
            'fields': (
                'call_date',
                'customer_care_specialist',
                'contact_information',
                'address_or_apn',
                'name_of_the_caller',
                'phone_number_of_caller',
                'are_you_an_agent',
                'listing',
                'your_phone_number',
                'email_address',
                'average_handling_time',
                'additional_notes',
            )
        }),
    )


admin.site.register(CustomerCareSpecialist)
admin.site.register(CygnusInvestment, CygnusInvestmentProfile)
admin.site.register(WeBuyAcreageLlc, WeBuyAcreageLlcProfile)