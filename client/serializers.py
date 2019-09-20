from rest_framework import serializers
from users.models import Staffs, Clients
from .models import Client, ClientLeadSource

from django.contrib.auth import get_user_model
User = get_user_model()


class LeadSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    virtual_assistant = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all())

    class Meta:
        model = ClientLeadSource
        fields = '__all__'

    def get_client(self, instance):
        return '%s - %s' % (instance.client.full_name, instance.client.company_name)
