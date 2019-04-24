import datetime

from decimal import Decimal

from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import VaPayroll
from django.db.models import Sum, Q, F

from .serializers import VaPayrollSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AddPayrollView(LoginRequiredMixin, ListView):
    template_name = 'payroll/add_payroll.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        user = request.user.staffs.full_name
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        payroll_list = VaPayroll.objects.all()
        payroll_data = payroll_list.filter(Q(virtual_assistant__name=user),
                                           Q(date__month=current_month))
        total_salary = VaPayroll.objects.filter(Q(virtual_assistant__name=user), 
                                                Q(date__month=search), 
                                                Q(date__year=current_year)).aggregate(Sum('salary'))
        if search:
            payroll_data = payroll_list.filter(Q(virtual_assistant__name=user),
                                               Q(date__icontains=search))
        
            payroll_data
        context = {
            'total_salary': total_salary,
            'payroll_data': payroll_data
        }   
        return render(request, self.template_name, context)


class SearchPayroll(LoginRequiredMixin, TemplateView):
    template_name = 'payroll/add_payroll.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = VaPayroll.objects.filter(date__icontains=q)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(result=self.results, **kwargs)

class PayrollViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VaPayrollSerializer

    def get_queryset(self):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        queryset = VaPayroll.objects.filter(Q(virtual_assistant__name=self.request.user.staffs.full_name), 
                                            Q(date__month=current_month), 
                                            Q(date__year=current_year))
        return queryset
