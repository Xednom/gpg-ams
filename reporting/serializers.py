from rest_framework import serializers
from .models import VATimeSheet


class VATimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VATimeSheet
        fields = '__all__'
