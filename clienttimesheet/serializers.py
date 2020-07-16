import datetime

from rest_framework import serializers
from .models import TimeSheet, PaymentMade, CashOut
from fillables.models import VirtualAssistant
from users.models import Clients, Staffs


class TimeSheetSerializer(serializers.ModelSerializer):
    clients_full_name = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Clients.objects.all())
    clients_full_name = serializers.StringRelatedField()
    assigned_approval = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(),
                                                     allow_null=True, required=False)
    time_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    time_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    client_control_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TimeSheet
        fields = '__all__'

    def get_client_control_number(self, obj):
        client_name = obj.client_full_name
        control_number = Clients.objects.filter(full_name=client_name).all()
        client_control_number = [client.client_control_number for client in control_number]
        return client_control_number


class PaymentMadeSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Clients.objects.all())

    class Meta:
        model = PaymentMade
        fields = '__all__'


class CashOutSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all())

    class Meta:
        model = CashOut
        fields = '__all__'
