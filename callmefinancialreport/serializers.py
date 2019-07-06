from rest_framework import serializers

from .models import FinancialReport
from users.models import Clients


class FinancialReportSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SlugRelatedField(slug_field='full_name', queryset=Clients.objects.all())

    class Meta:
        model = FinancialReport
        fields = '__all__'