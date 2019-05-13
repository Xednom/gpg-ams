import datetime
import django_filters

from decimal import Decimal

from django_filters.rest_framework import FilterSet
from django_filters import DateRangeFilter, DateFilter, CharFilter, NumberFilter
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from django.db.models import Sum, Q, F

from .models import VaPayroll, VaCashOut
from .forms import PayrollCreateForm
from .serializers import VaPayrollSerializer, VaCashOutSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PayrollView(LoginRequiredMixin, TemplateView):
    template_name = 'payroll/view_payroll.html'
    model = VaPayroll
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        user = request.user.staffs.full_name
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        payroll_list = VaPayroll.objects.all()
        payroll_data = payroll_list.filter(Q(virtual_assistant=user),
                                           Q(date__month=current_month),
                                           Q(status='APPROVED-BY-THE-MANAGER'))
        total_salary = VaPayroll.objects.filter(Q(virtual_assistant=user), 
                                                Q(date__month=current_month),
                                                Q(status='APPROVED-BY-THE-MANAGER'),
                                                Q(date__year=current_year)).aggregate(Sum('salary'))
        if search:
            payroll_data = payroll_list.filter(Q(virtual_assistant=user),
                                               Q(status='APPROVED-BY-THE-MANAGER'),
                                               Q(date__icontains=search))
            total_salary = VaPayroll.objects.filter(Q(virtual_assistant=user),
                                                    Q(status='APPROVED-BY-THE-MANAGER'),
                                                    Q(date__month=search),
                                                    Q(date__year=current_year)).aggregate(Sum('salary'))
        context = {
            'total_salary': total_salary,
            'payroll_data': payroll_data
        }
        return render(request, self.template_name, context)


class AddPayroll(SuccessMessageMixin, CreateView):
    template_name = 'payroll/add_payroll.html'
    model = VaPayroll
    fields = ['date', 'virtual_assistant', 'time_in', 'time_out', 'client_name', 'rate']
    # form_class = PayrollCreateForm
    success_message = "Successfully added a payroll."

    def form_valid(self, form):
        form.instance.virtual_assistant = self.request.user.staffs.full_name
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("payroll:add_payroll")


class PayrollFilters(FilterSet):
    date__month = NumberFilter(field_name='date', lookup_expr='month')
    virtual_assistant = CharFilter(field_name='virtual_assistant', lookup_expr='icontains')

    class Meta:
        model = VaPayroll
        fields = ('date__month', 'virtual_assistant')


class CashOutFilters(FilterSet):
    date_release__month = NumberFilter(field_name='date_release', lookup_expr='month')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = VaCashOut
        fields = ('date_release__month', 'name')


class PayrollViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VaPayrollSerializer
    filter_class = (PayrollFilters)
    filterset_fields = ('date',)
    search_fields = ('date',)

    def get_queryset(self):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        queryset = VaPayroll.objects.filter(Q(virtual_assistant=self.request.user.staffs.full_name), 
                                            Q(date__year=current_year),
                                            Q(status='APPROVED-BY-THE-MANAGER'))
        return queryset


class PayrollCashOutViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VaCashOutSerializer
    filter_class = (CashOutFilters)
    filterset_fields = ('date_release',)
    search_fields = ('date_release',)

    def get_queryset(self):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        queryset = VaCashOut.objects.filter(Q(name__name=self.request.user.staffs.full_name),
                                            Q(date_release__year=current_year))
        return queryset
