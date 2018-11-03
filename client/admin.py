from django.contrib import admin
from .models import (
    CompanyCategory,
    ClientName,
    Lead,
    ProjectManager,
    SeniorManager,
    TypeOfTask,
    StatusChoice,
    Client
    )


class ClientProfile(admin.ModelAdmin):
    list_display = ['client', 'client_code', 'company_category_under', 'clients_company_name', 'client_email', 'lead_source', 'clients_project_manager', 'status']
    fieldsets = (
        (None, {
            'fields': ('date_sign_up',)
        }),
        ('Client information', {
            'fields': (
                'company_category_under',
                'clients_company_name',
                'client',
                'client_code',
                'client_phone_number',
                'client_email',
                'lead_source',
                'clients_project_manager',
                'clients_count_number',
                'status',
            )
        }),
        ('Hour rate agreed', {
            'fields': ('agreed_hourly_rate',)
        }),
        ('G.P.G consultant informations', {
            'fields': ('VA_assigned', 'type_of_task', 'senior_manager', 'notes')
        })
    )


admin.site.register(CompanyCategory)
admin.site.register(ClientName)
admin.site.register(Lead)
admin.site.register(ProjectManager)
admin.site.register(SeniorManager)
admin.site.register(TypeOfTask)
admin.site.register(StatusChoice)
admin.site.register(Client, ClientProfile)
