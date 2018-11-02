from rest_framework import serializers
from .models import Client, ClientName, ProjectManager, SeniorManager, TypeOfTask

from django.contrib.auth import get_user_model
User = get_user_model()


class ClientSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='name', queryset=ClientName.objects.all())
    clients_project_manager = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())
    senior_manager = serializers.SlugRelatedField(slug_field='name', queryset=SeniorManager.objects.all())
    type_of_task = serializers.SlugRelatedField(slug_field='task_name', queryset=TypeOfTask.objects.all())
    VA_assigned = serializers.SlugRelatedField(slug_field='full_name', queryset=User.objects.all())

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
            'type_of_task',
            'status',
            'notes'
        )
