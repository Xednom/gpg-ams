import datetime

from rest_framework import serializers
from .models import VaPayroll

from fillables.models import VirtualAssistant


class VaPayrollSerializer(serializers.ModelSerializer):
    virtual_assistant = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all())
    time_in = serializers.DateTimeField()
    time_out = serializers.DateTimeField()

    class Meta:
        model = VaPayroll
        fields = '__all__'