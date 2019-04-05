from django.contrib import admin

from .models import Logins


class LoginsProfile(admin.ModelAdmin):
    list_display = ('client_full_name', 'company_name', 'type_of_apps', 'give_access_to')
    search_fields = ('client_full_name', 'company_name', 'type_of_apps', 'give_access_to')
    fieldsets = (
        ("Login Informations", {
            'fields': (
                'client_full_name',
                'company_name',
                'type_of_apps',
                'link_to_the_app',
                'user_name',
                'password',
                'give_access_to',
                'notes',
            )
        }),
    )

admin.site.register(Logins, LoginsProfile)