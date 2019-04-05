from rest_framework import serializers

from .models import Logins
from fillables.models import VirtualAssistant


class LoginsSerializer(serializers.ModelSerializer):
    give_access_to = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Logins
        fields = '__all__'
