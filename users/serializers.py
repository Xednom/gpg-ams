import datetime

from rest_framework import serializers
from .models import Clients, Staffs, Email


class EmailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Email
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    email = EmailSerializer()
    
    class Meta:
        model = Clients
        fields = '__all__'
    
    def get_client_name_company_name(self, obj):
        return '%s - %s' % (obj.Clients.full_name, obj.Clients.company_name)


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staffs
        fields = ('full_name',)
