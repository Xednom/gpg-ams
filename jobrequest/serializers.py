from rest_framework import serializers

from client.models import ProjectManager
from .models import JobRequest


class JobRequestSerializer(serializers.ModelSerializer):
    project_managers = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())

    class Meta:
        model = JobRequest
        fields = '__all__'
