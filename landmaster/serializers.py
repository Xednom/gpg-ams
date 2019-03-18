import datetime

from rest_framework import serializers
from .models import DueDiligence

from fillables.models import CompanyName


class DueDiligenceSerializer(serializers.ModelSerializer):
    date_requested = serializers.DateField(default=datetime.date.today)
    company_name = serializers.SlugRelatedField(slug_field='name', queryset=CompanyName.objects.all())

    class Meta:
        model = DueDiligence
        fields = '__all__'