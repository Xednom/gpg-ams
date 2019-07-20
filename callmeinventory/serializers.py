from rest_framework import serializers

from .models import inventory
from users.models import Staffs


class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = inventory
        fields = '__all__'