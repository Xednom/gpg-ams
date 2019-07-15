import datetime

from rest_framework import serializers

from django.utils.timezone import now

from users.models import Staffs, Clients
from fillables.models import JobTitleRequest, VirtualAssistant
from .models import JobRequest, JobRequestTimeSheet


class JobTitleRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitleRequest
        fields = ('title',)


class JobRequestSerializer(serializers.ModelSerializer):
    assigned_va = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    assigned_project_managers = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    date_requested = serializers.DateField(default=datetime.date.today)
    due_date = serializers.DateField(default=datetime.date.today)

    class Meta:
        model = JobRequest
        fields = '__all__'


class TimeSheetSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    client = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all(), allow_null=True, required=False)
    job_title = serializers.SlugRelatedField(slug_field='job_request_title', queryset=JobRequest.objects.all(), allow_null=True, required=False)
    time_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    time_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    total_minutes_hours = serializers.DecimalField(max_digits=7, decimal_places=2, read_only=True)

    class Meta:
        model = JobRequestTimeSheet
        fields = '__all__'
