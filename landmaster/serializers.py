import datetime

from rest_framework import serializers
from .models import DueDiligence, DueDiligencesCleared

from fillables.models import CompanyName, VirtualAssistant, ProjectManager


class VaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VirtualAssistant
        fields = '__all__'


class DueDiligenceSerializer(serializers.ModelSerializer):
    dd_va_assigned_initial_data = serializers.SlugRelatedField(
        slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_tax_data = serializers.SlugRelatedField(
        slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_zoning_data = serializers.SlugRelatedField(
        slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_utilities_data = serializers.SlugRelatedField(
        slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_other_requests = serializers.SlugRelatedField(
        slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)
    project_manager = serializers.SlugRelatedField(slug_field='project_manager', queryset=ProjectManager.objects.all(), allow_null=True, required=False)
    date_completed = serializers.DateField(allow_null=True, required=False)
    date_completed_initial_dd_time_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_initial_dd_time_out = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_tax_data_time_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_tax_data_time_out = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_zoning_data_time_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_zoning_data_time_out = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_utilities_time_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_utilities_time_out = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_other_requests_time_in = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")
    date_completed_other_requests_time_out = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M")

    class Meta:
        model = DueDiligence
        fields = '__all__'


class DueDiligenceClearedSerializer(serializers.ModelSerializer):
    call_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    call_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = DueDiligencesCleared
        fields = '__all__'
