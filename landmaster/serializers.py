import datetime

from rest_framework import serializers
from .models import DueDiligence

from fillables.models import CompanyName


class DueDiligenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DueDiligence
        fields = '__all__'