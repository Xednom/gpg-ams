from rest_framework import serializers

from .models import O20SmartPricing, LandAcademyInventory
from users.models import Staffs, Clients


class LandAcademySerializer(serializers.ModelSerializer):

    class Meta:
        model = LandAcademyInventory
        fields = '__all__'


class SmartPricingSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field="full_name", queryset=Clients.objects.all(),
                                                     allow_null=True, required=False)
    virtual_assistant = serializers.SlugRelatedField(slug_field="full_name", queryset=Staffs.objects.all(), \
                                                   allow_null=True, required=False)

    class Meta:
        model = O20SmartPricing
        fields = '__all__'
