from django.contrib import admin

# Register your models here.

# class StaffProfile(admin.ModelAdmin):
#     list_display = ('user_name', 'full_name', 
#                     'phone_number', 'SSS_number', 
#                     'TIN_number', 'pag_ibig_number', 
#                     'philhealth', 'position', 'status')
#     list_filter = ('full_name', 'position', 'status')
#     search_fields = ('full_name', 'position', 'SSS_number',
#                      'TIN_number', 'pag_ibig_number')
#     fieldsets = (
#         ('Staff Informations', {
#             'fields': (
#                 'user_name',
#                 'full_name',
#                 'phone_number',
#                 'SSS_number',
#                 'TIN_number',
#                 'pag_ibig_number',
#                 'philhealth',
#                 'position',
#                 'id_number',
#                 'status',
#                 'notes',
#             )
#         }),
#         ('Personal Informations', {
#             'fields': (
#                 'date_of_birth',
#                 'blood_type',
#                 'mother_full_maiden_name',
#                 'father_full_name',
#                 'emergency_contact_name',
#                 'emergency_contact_number',
#                 'relationship_to_the_emergency_contact_person',
#                 'residential_address',
#             )
#         }),
#     )


# class ClientProfile(admin.ModelAdmin):
#     list_display = ('username','full_name', 'company_name')
#     list_filter = ['company_name']
#     search_fields = ('username', 'full_name', 'company_name')
#     fieldsets = (
#         ('Client Informations', {
#             'fields': (
#                 'username',
#                 'full_name',
#                 'company_name',
#             )
#         }),
#     )

# admin.site.register(Staffs, StaffProfile)
# admin.site.register(Clients, ClientProfile)