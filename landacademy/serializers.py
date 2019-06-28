from rest_framework import serializers

from .models import O20SmartPricing, LandAcademyInventory


class LandAcademySerializer(serializers.ModelSerializer):

    class Meta:
        model = LandAcademyInventory
        fields = '__all__'


class SmartPricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = O20SmartPricing
        fields = '__all__'
