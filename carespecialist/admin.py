from django.contrib import admin
# from .models import CareSpecialistReport


# class CareSpecialistProfile(admin.ModelAdmin):
#     list_display = ('care_specialist', 'name_appeared_from_letter', 'date_of_the_lead_called', 'caller_id', 'total_minutes_answered')
#     list_filter = ('care_specialist',)
#     list_per_page = 20
#     search_fields = ('care_specialist', 'name_appeared_from_letter')
#     fieldsets = (
#         (None, {
#             'fields': ('date_of_the_lead_called',)
#         }),
#         ('Care Specialist report Information', {
#             'fields': (
#                 'name_appeared_from_letter',
#                 'care_specialist',
#                 'full_name_of_the_caller',
#                 'caller_id',
#                 'phone_number',
#                 'receive_letter',
#                 'notes',
#                 'property_located',
#                 'apn_property_id',
#                 'selling_property',
#                 'price_looking_to_get_property',
#                 'owner_of_the_property',
#                 'name_on_the_record',
#                 'mailed_from',
#                 'mailing_address',
#                 'contact_number',
#                 'email_address',
#                 'properties',
#                 'apn_counties',
#                 'taxes',
#                 'total_current_amount_due',
#                 'special_attribute',
#                 'info_on_the_property',
#                 'extra_comments',
#                 'email_sent_to_the_owner',
#                 'calendar_invite',
#                 'total_minutes_answered'
#             )
#         }
#         )
#     )


# admin.site.register(CareSpecialistReport, CareSpecialistProfile)
