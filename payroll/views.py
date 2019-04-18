from decimal import Decimal

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import VaPayroll
from django.db.models import Sum

from .serializers import VaPayrollSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AddPayrollView(LoginRequiredMixin, View):
    template_name = 'payroll/add_payroll.html'

    def get(self, request, *args, **kwargs):
        user = request.user.staffs.full_name
        total_salary = VaPayroll.objects.filter(virtual_assistant__name=user).aggregate(Sum('salary'))
        context = {
            'total_salary': total_salary
        }
        return render(request, self.template_name, context)


class PayrollViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VaPayrollSerializer

    def get_queryset(self):
        queryset = VaPayroll.objects.filter(virtual_assistant__name=self.request.user.staffs.full_name)
        return queryset
