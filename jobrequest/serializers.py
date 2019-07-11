import datetime

from rest_framework import serializers

from django.utils.timezone import now

from users.models import Staffs
from fillables.models import JobTitleRequest, VirtualAssistant
from .models import JobRequest


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
