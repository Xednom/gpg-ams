from rest_framework import serializers

from .models import AdsContent
from users.models import Clients, Staffs

class AdsSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Clients.objects.all(), allow_null=True, required=False)
    ads_writer = serializers.SlugRelatedField(
        slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)

    class Meta:
        model = AdsContent
        fields = '__all__'
