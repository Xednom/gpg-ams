from django.contrib import admin

from .models import Logins


class LoginsProfile(admin.ModelAdmin):
    list_display = ('client_full_name', 'company_name', 'type_of_apps', 'give_access_to')
    search_fields = ('client_full_name', 'company_name', 'type_of_apps', 'give_access_to')
    readonly_fields = ('added_by', 'updated_by')
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
                'added_by',
                'updated_by',
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, save the user who will add this
            obj.added_by = request.user.staffs.full_name
        elif change:
            obj.updated_by = request.user.staffs.full_name
        obj.save()

admin.site.register(Logins, LoginsProfile)
