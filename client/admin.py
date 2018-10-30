from django.contrib import admin
from .models import (
    CompanyCategory,
    ClientName,
    Lead,
    ProjectManager,
    SeniorManager,
    TypeOfTask,
    Client
    )


class ClientProfile(admin.ModelAdmin):
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
                'clients_project_manager',
                'clients_count_number',
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
admin.site.register(Client, ClientProfile)
