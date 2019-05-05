import datetime

from django.db.models import Q, Sum
from rest_framework import serializers
from .models import VaPayroll, VaCashOut

from fillables.models import VirtualAssistant


class VaPayrollSerializer(serializers.ModelSerializer):
    total_salary = serializers.SerializerMethodField()
    time_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    time_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = VaPayroll
        fields = '__all__'

    def get_total_salary(self, obj):
        user = self.context['request'].user.staffs.full_name
        totalsalary = VaPayroll.objects.filter(Q(status='APPROVED-BY-THE-MANAGER'),
                                               Q(virtual_assistant=user),
                                               Q(date__month=datetime.date.today().month),
                                               Q(date__year=datetime.date.today().year)).aggregate(total_salary=Sum('salary'))
        return totalsalary['total_salary']


class VaCashOutSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(slug_field='name', queryset=VirtualAssistant.objects.all())

    class Meta:
        model = VaCashOut
        fields = '__all__'
