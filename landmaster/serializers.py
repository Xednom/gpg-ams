import datetime

from rest_framework import serializers
from .models import DueDiligence, DueDiligencesCleared

from fillables.models import CompanyName, VirtualAssistant, ProjectManager

from users.models import Staffs, Clients
from users.serializers import StaffSerializer


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
    client_full_name = serializers.SlugRelatedField(slug_field='full_name', allow_null=True, required=False,
                                                    queryset=Clients.objects.filter(company_category='landmaster.us'))
    customer_service_representative = serializers.SlugRelatedField(slug_field='full_name', allow_null=True, required=False,
                                                    queryset=Staffs.objects.all())
    class Meta:
        model = DueDiligencesCleared
        fields = '__all__'
