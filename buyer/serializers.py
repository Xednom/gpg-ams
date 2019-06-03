import datetime

from rest_framework import serializers

from .models import CustomerCareSpecialist


class CustomerCareSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerCareSpecialist
        fields = '__all__'
