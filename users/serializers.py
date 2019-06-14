import datetime

from rest_framework import serializers
from .models import Clients, Staffs


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clients
        fields = ('full_name',)


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staffs
        fields = ('full_name',)
