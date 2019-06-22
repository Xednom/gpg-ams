from rest_framework import serializers

from .models import MasterBoard
from users.models import Clients


class MasterBoardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MasterBoard
        fields = '__all__'