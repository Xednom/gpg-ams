from rest_framework import serializers
from .models import JobRequest


class JobRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequest
        fields = '__all__'
