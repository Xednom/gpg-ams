from rest_framework import serializers

from client.models import ProjectManager
from .models import JobRequest, StatusOfTheJobRequest


class StatusOfTheJobRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOfTheJobRequest
        fields = ('type_of_status',)


class JobRequestSerializer(serializers.ModelSerializer):
    status_of_the_job_request = serializers.SlugRelatedField(slug_field='type_of_status', queryset=StatusOfTheJobRequest.objects.all())
    project_managers = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())

    class Meta:
        model = JobRequest
        fields = '__all__'
