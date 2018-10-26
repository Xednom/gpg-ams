from django.contrib import admin
from .models import (
    CompanyCategory,
    ClientName,
    Lead,
    ProjectManager,
    TypeOfTask,
    Client
    )


class ClientProfile(admin.ModelAdmin):
    list_display = (
        'date_sign_up',
        'company_category_under',
         'clients_company_name',
         'agreed_hourly_rate',
         'client',
         'client_code',
         'client_phone_number',
         'client_email',
         'lead_source',
         'referred_by',
         'clients_project_manager',
         'clients_count_number',
         'VA_assigned',
         'type_of_task',
         'notes'
         )


admin.site.register(CompanyCategory)
admin.site.register(ClientName)
admin.site.register(Lead)
admin.site.register(ProjectManager)
admin.site.register(TypeOfTask)
admin.site.register(Client, ClientProfile)
