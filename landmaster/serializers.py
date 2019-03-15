import datetime

from rest_framework import serializers
from .models import (
    DueDiligence,
    LandData,
    AdditionalLandInfo,
    CountyData,
    TaxData,
    ZoningData,
    DataOnUtilities,
)

from fillables.models import CompanyName


class DueDiligenceSerializer(serializers.ModelSerializer):
    date_requested = serializers.DateField(default=datetime.date.today)
    company_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = DueDiligence
        fields = '__all__'


class LandDataSerializer(serializers.ModelSerializer):
    owner_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = LandData
        fields = '__all__'


class AdditionalLandInfoSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = AdditionalLandInfo
        fields = '__all__'

    
class CountyDataSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = CountyData
        fields = '__all__'


class TaxDataSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = TaxData
        fields = '__all__'

    
class ZoningDataSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = ZoningData
        fields = '__all__'


class DataOnUtilitiesSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = DataOnUtilities
        fields = '__all__'