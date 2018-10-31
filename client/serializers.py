from rest_framework import serializers
from .models import Client, ProjectManager, SeniorManager

from django.conf import settings


class ClientSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='client_name', queryset=Client.objects.all())
    clients_project_manager = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())
    senior_manager = serializers.SlugRelatedField(slug_field='name', queryset=SeniorManager.objects.all())

    class Meta:
        model = Client
        fields = (
            'clients_company_name',
            'client_code',
            'client',
            'client_phone_number',
            'client_email',
            'clients_project_manager',
            'senior_manager',
            'VA_assigned',
            'status',
            'notes'
        )
