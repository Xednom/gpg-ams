import datetime

from rest_framework import serializers
from .models import TimeSheet, PaymentMade, CashOut
from fillables.models import VirtualAssistant
from users.models import Clients, Staffs

class TimeSheetSerializer(serializers.ModelSerializer):
    clients_full_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all())
    assigned_va = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all())
    assigned_pm = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all())
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

    class Meta:
        model = CashOut
        fields = '__all__'
