from .models import Inventory

from rest_framework import serializers


class InventorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'