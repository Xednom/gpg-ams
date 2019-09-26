from rest_framework import serializers
from users.models import Staffs, Clients
from .models import Client, ClientLeadSource

from django.contrib.auth import get_user_model
User = get_user_model()


class LeadSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Clients.objects.all(), allow_null=True, required=False)
    virtual_assistant = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)

    class Meta:
        model = ClientLeadSource
        fields = '__all__'

    def get_client(self, instance):
        return '%s - %s' % (instance.client.full_name, instance.client.company_name)
