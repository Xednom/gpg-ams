import datetime

from rest_framework import serializers
from .models import DueDiligence

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
