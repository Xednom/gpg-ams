from django.contrib import admin
from .models import Client
from fillables.models import (
    InternalCompanyName,
    CompanyName,
    LeadSource,
    ProjectManager,
    SeniorManager,
    TypeOfTask
    )


class ClientProfile(admin.ModelAdmin):
    list_display = ('company_name', 'client_code', 'company_category_under', 'client_company_name', 'client_email', 'lead_source', 'clients_project_manager', 'status')
    list_filter = ('status',)
    list_per_page = 15
    search_fields = ('client_code', 'company_name', 'client_company_name')
    # change_list_template = 'client/change_list_graph.html'
    fieldsets = (
        (None, {
            'fields': ('date_sign_up',)
        }),
        ('Client information', {
            'fields': (
                'company_category_under',
                'client_company_name',
                'company_name',
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


admin.site.register(InternalCompanyName)
admin.site.register(CompanyName)
admin.site.register(LeadSource)
admin.site.register(ProjectManager)
admin.site.register(SeniorManager)
admin.site.register(TypeOfTask)
admin.site.register(Client, ClientProfile)
