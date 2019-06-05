import datetime

from django.db.models import Q, Sum
from rest_framework import serializers

from .models import AffordableLandInvestment
from buyer.models import CustomerCareSpecialist


class AffordableLandSerializer(serializers.ModelSerializer):
    customer_care_specialist = serializers.SlugRelatedField(slug_field='name', queryset=CustomerCareSpecialist.objects.all())
    call_date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = AffordableLandInvestment
        fields = '__all__'
