from django.contrib import admin

from .models import Logins
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .resources import LoginsResource


class LoginsProfile(ImportExportModelAdmin):
    list_display = ('company_category', 'client_full_name',
                    'company_name', 'apps_url_link', 'user_name',
                    'password', 'added_by')
    list_filter = ('client_full_name', 'company_name', 
                   'company_category', 'give_access_to')
    list_per_page = 30
    search_fields = ('client_full_name__name', 'company_name', 'type_of_apps', 'give_access_to__full_name')
    readonly_fields = ('date_created', 'added_by', 'updated_by')
    resource_class = LoginsResource
    fieldsets = (
        ("Login Informations", {
            'fields': (
                'client_full_name',
                'company_name',
                'company_category',
                'type_of_apps',
                'link_to_the_app',
                'apps_url_link',
                'user_name',
                'password',
                'give_access_to',
                'notes',
            )
        }),
        ("Important informations", {
            'fields': (
                'date_created',
                'added_by',
                'updated_by',
            )
        })
    )

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         # the object is being created, save the user who will add this
    #         obj.added_by = request.user
    #     elif change:
    #         obj.updated_by = request.user
    #     obj.save()

admin.site.register(Logins, LoginsProfile)
