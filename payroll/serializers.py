import datetime

from django.db.models import Q, Sum
from rest_framework import serializers
from .models import VaPayroll

from fillables.models import VirtualAssistant


class VaPayrollSerializer(serializers.ModelSerializer):
    total_salary = serializers.SerializerMethodField()

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
