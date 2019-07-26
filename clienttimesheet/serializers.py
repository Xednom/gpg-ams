import datetime

from rest_framework import serializers
from .models import TimeSheet, PaymentMade, CashOut
from fillables.models import VirtualAssistant
from users.models import Clients, Staffs

class TimeSheetSerializer(serializers.ModelSerializer):
    clients_full_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all())
    clients_full_name = serializers.StringRelatedField()
    assigned_va = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), 
                                               allow_null=True, required=False)
    assigned_pm = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), 
                                               allow_null=True, required=False)
    time_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    time_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = TimeSheet
        fields = '__all__'
    

class PaymentMadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMade
        fields = '__all__'


class CashOutSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all())

    class Meta:
        model = CashOut
        fields = '__all__'
