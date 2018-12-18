from rest_framework import serializers
from .models import Client, CompanyName, ProjectManager, SeniorManager, TypeOfTask

from django.contrib.auth import get_user_model
User = get_user_model()


class ClientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyName
        fields = ('name',)


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ('project_manager',)


class TypeOfTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTask
        fields = ('task_name',)


class SeniorManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeniorManager
        fields = ('name',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name',)


class ClientSerializer(serializers.ModelSerializer):
    company_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())
    clients_project_manager = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())
    senior_manager = serializers.SlugRelatedField(slug_field='name', queryset=SeniorManager.objects.all())
    type_of_task = serializers.SlugRelatedField(slug_field='task_name', queryset=TypeOfTask.objects.all())
    VA_assigned = serializers.SlugRelatedField(slug_field='full_name', queryset=User.objects.all())

    class Meta:
        model = Client
        fields = (
            'id',
            'clients_company_name',
            'client_code',
            'company_name',
            'client_phone_number',
            'client_email',
            'clients_project_manager',
            'senior_manager',
            'VA_assigned',
            'type_of_task',
            'status',
            'notes'
        )
