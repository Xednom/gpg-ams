from rest_framework import serializers

from client.models import ProjectManager
from fillables.models import JobTitleRequest, VirtualAssistant
from .models import JobRequest


class JobTitleRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitleRequest
        fields = ('title',)


class JobRequestSerializer(serializers.ModelSerializer):
    assigned_va = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    assigned_project_managers = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all(), allow_null=True, required=False)

    class Meta:
        model = JobRequest
        fields = '__all__'
