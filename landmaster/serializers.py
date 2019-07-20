import datetime

from rest_framework import serializers
from .models import DueDiligence, DueDiligencesCleared

from fillables.models import CompanyName, VirtualAssistant, ProjectManager

from users.models import Staffs


class VaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VirtualAssistant
        fields = '__all__'


class DueDiligenceSerializer(serializers.ModelSerializer):
    dd_va_assigned_initial_data = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_tax_data = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_zoning_data = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_utilities_data = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    dd_va_assigned_call_outs_other_requests = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    project_manager = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)

    class Meta:
        model = DueDiligence
        fields = '__all__'


class DueDiligenceClearedSerializer(serializers.ModelSerializer):
    call_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    call_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = DueDiligencesCleared
        fields = '__all__'
