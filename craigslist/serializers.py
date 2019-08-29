from rest_framework import serializers

from .models import CraiglistInventory

from users.models import Staffs, Clients
from users.serializers import ClientSerializer


class ClientAndCompanyNameField(serializers.RelatedField):
    def to_representation(self, value):
        return '%s - %s' % (value.full_name, value.company_name)
    
    def to_internal_value(self, value):
        return value

    def get_queryset(self):
        clients_list = Clients.objects.all()
        return clients_list


class CraigListSerializer(serializers.ModelSerializer):

    client_name_company_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all(), allow_null=True)
    cl_admin_support = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True)

    class Meta:
        model = CraiglistInventory
        fields = '__all__'