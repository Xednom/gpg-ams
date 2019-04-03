from rest_framework import serializers

from client.models import ProjectManager
from fillables.models import JobTitleRequest
from .models import JobRequest


class JobTitleRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitleRequest
        fields = ('title',)


class JobRequestSerializer(serializers.ModelSerializer):
    assigned_project_managers = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all())

    class Meta:
        model = JobRequest
        fields = '__all__'
