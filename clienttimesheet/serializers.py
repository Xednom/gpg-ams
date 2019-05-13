import datetime

from rest_framework import serializers
from .models import TimeSheet, PaymentMade

from fillables.models import VirtualAssistant


class TimeSheetSerializer(serializers.ModelSerializer):
    assigned_job_request_to = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all())

    class Meta:
        model = TimeSheet
        fields = '__all__'
    

class PaymentMadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMade
        fields = '__all__'
