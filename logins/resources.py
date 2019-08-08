from import_export import resources
from import_export.fields import Field

from .models import Logins


class LoginsResource(resources.ModelResource):

    class Meta:
        model = Logins
        fields = (
            'client_full_name__full_name',
            'company_name', 'company_category', 'apps_url_link',
            'type_of_apps', 'link_to_the_app', 'user_name',
            'password', 'notes', 'give_access_to',
            'date_created', 'added_by', 'updated_by'
        )
        export_order = (
            'client_full_name__full_name',
            'company_name', 'company_category', 'apps_url_link',
            'type_of_apps', 'link_to_the_app', 'user_name',
            'password', 'notes', 'give_access_to',
            'date_created', 'added_by', 'updated_by'
        )
