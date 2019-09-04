from rest_framework import serializers

from .models import inventory
from users.models import Staffs, Clients


class InventorySerializer(serializers.ModelSerializer):
    client_full_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all())
    
    class Meta:
        model = inventory
        fields = '__all__'