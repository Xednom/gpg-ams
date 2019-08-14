import datetime
import django_filters

from django.shortcuts import render


from django_filters.rest_framework import FilterSet
from django_filters import DateRangeFilter, DateFilter, CharFilter, NumberFilter
from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import TimeSheet, PaymentMade, CashOut
from .serializers import TimeSheetSerializer, PaymentMadeSerializer, CashOutSerializer


class AddVaTimeSheetView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'timesheet/add_timesheet.html'
    model = TimeSheet
    fields = [
        'company_tagging', 'shift_date', 'month_to_date', 'clients_full_name',
        'title_job_request', 'channel_job_requested', 'job_request_description',
        'time_in', 'time_out', 'total_items', 'additional_comments', 'hourly_rate_peso',
        'status', 'assigned_va', 'assigned_pm'
    ]
    success_message = "Successfully added a timesheet!"
    
    def form_valid(self, form):
        if self.request.user.staffs.position == 'Project Manager':
            form.instance.assigned_pm = self.request.user.staffs
            return super().form_valid(form)
        elif self.request.user.staffs.position == 'General Administrative Support':
            form.instance.assigned_va = self.request.user.staffs
            return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('timesheet:add_timesheet')


class VaTimeSheetView(TemplateView, LoginRequiredMixin):
    template_name = 'timesheet/va_timesheet.html'


class TimeSheetView(TemplateView, LoginRequiredMixin):
    template_name = 'timesheet/view_timesheet.html'


class TimeSheetFilter(FilterSet):
    shift_date__month = NumberFilter(field_name='shift_date', lookup_expr='month')
    company_tagging = CharFilter(field_name='company_tagging', lookup_expr='icontains')

    class Meta:
        model = TimeSheet
        fields = ('shift_date__month', 'company_tagging')

    
class PaymentMadeFilter(FilterSet):
    date__month = NumberFilter(field_name='date', lookup_expr='month')
    name = CharFilter(field_name='client_name', lookup_expr='icontains')

    class Meta:
        model = PaymentMade
        fields = ('date__month', 'name')


class CashOutFilter(FilterSet):
    cash_date_release__month = NumberFilter(field_name='cash_date_release', lookup_expr='month')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = CashOut
        fields = ('cash_date_release__month', 'name')


class TimeSheetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSheetSerializer
    filter_class = (TimeSheetFilter)

    def get_queryset(self):
        current_year = datetime.date.today().year
        if self.request.user.is_client:
            queryset = TimeSheet.objects.filter(Q(clients_full_name__full_name__icontains=self.request.user.clients.full_name),
                                                Q(shift_date__year=current_year),
                                                Q(admin_approval="Approved"))
            return queryset
        elif self.request.user.is_staffs:
            queryset = TimeSheet.objects.filter(Q(assigned_va__full_name__icontains=self.request.user.staffs.full_name) |
                                                Q(assigned_pm__full_name__icontains=self.request.user.staffs.full_name),
                                                Q(shift_date__year=current_year))
            return queryset


class PaymentMadeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentMadeSerializer
    filter_class = (PaymentMadeFilter)

    def get_queryset(self):
        current_year = datetime.date.today().year
        if self.request.user.is_client:
            queryset = PaymentMade.objects.filter(Q(client_name__full_name=self.request.user.clients.full_name),
                                                  Q(date__year=current_year))
            return queryset


class CashOutViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashOutSerializer
    filter_class = (CashOutFilter)

    def get_queryset(self):
        current_year = datetime.date.today().year
        if self.request.user.is_staffs:
            queryset = CashOut.objects.filter(Q(name__full_name=self.request.user.staffs.full_name),
                                              Q(cash_date_release__year=current_year))
            return queryset
