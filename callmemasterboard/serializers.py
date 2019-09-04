from rest_framework import serializers

from .models import MasterBoard
from users.models import Clients


class MasterBoardSerializer(serializers.ModelSerializer):
    client_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all())
    
    class Meta:
        model = MasterBoard
        fields = '__all__'