from rest_framework import serializers

from .models import Logins
from users.models import Staffs, Clients


class LoginsSerializer(serializers.ModelSerializer):
    give_access_to = serializers.SlugRelatedField(slug_field='full_name', queryset=Staffs.objects.all(), allow_null=True, required=False)
    client_full_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Logins
        fields = '__all__'
