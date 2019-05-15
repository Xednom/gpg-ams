import datetime

from rest_framework import serializers
from .models import ManagerReminders


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManagerReminders
        fields = '__all__'