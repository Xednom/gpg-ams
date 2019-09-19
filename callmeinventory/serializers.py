from rest_framework import serializers

from .models import inventory, VaForm
from users.models import Staffs, Clients


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = inventory
        fields = '__all__'


class VaFormSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()

    class Meta:
        model = VaForm
        fields = '__all__'

    def get_client_full_name(self, instance):
        return '%s - %s' % (instance.client_full_name.full_name, instance.client_full_name.company_name)
