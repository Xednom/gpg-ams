import datetime

from rest_framework import serializers
from .models import DueDiligence, DueDiligencesCleared

from fillables.models import CompanyName, VirtualAssistant, ProjectManager


class VaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VirtualAssistant
        fields = '__all__'


class DueDiligenceSerializer(serializers.ModelSerializer):
    dd_team_assigned_va = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    project_manager = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all(), allow_null=True, required=False)

    class Meta:
        model = DueDiligence
        fields = '__all__'


class DueDiligenceClearedSerializer(serializers.ModelSerializer):
    call_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    call_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = DueDiligencesCleared
        fields = '__all__'
