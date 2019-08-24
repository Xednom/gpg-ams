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
        'status', 'assigned_approval'
    ]
    success_message = "Successfully added a timesheet!"

    def form_valid(self, form):
        form.instance.assigned_approval = self.request.user.staffs
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('timesheet:add_timesheet')


class VaTimeSheetView(TemplateView, LoginRequiredMixin):
    template_name = 'timesheet/va_timesheet.html'


class TimeSheetView(TemplateView, LoginRequiredMixin):
    template_name = 'timesheet/view_timesheet.html'


class TimeSheetMasterView(TemplateView, LoginRequiredMixin):
    template_name = 'timesheet/masterboard.html'


class TimeSheetFilter(FilterSet):
    shift_date__month = NumberFilter(
        field_name='shift_date', lookup_expr='month')
    shift_date__gte = DateFilter(field_name='shift_date', lookup_expr='gte')
    shift_date__lte = DateFilter(field_name='shift_date', lookup_expr='lte')
    assigned_approval__full_name = CharFilter(
        field_name='assigned_approval__full_name', lookup_expr='icontains')
    clients_full_name = CharFilter(
        field_name='clients_full_name__full_name', lookup_expr='icontains')

    class Meta:
        model = TimeSheet
        fields = (
            'shift_date__month',
            'assigned_approval__full_name',
            'clients_full_name',
            'shift_date__gte',
            'shift_date__lte',
        )


class PaymentMadeFilter(FilterSet):
    date__month = NumberFilter(field_name='date', lookup_expr='month')
    name = CharFilter(field_name='client_name__full_name', lookup_expr='icontains')

    class Meta:
        model = PaymentMade
        fields = ('date__month', 'name')


class CashOutFilter(FilterSet):
    cash_date_release__month = NumberFilter(
        field_name='cash_date_release', lookup_expr='month')
    name = CharFilter(field_name='name__full_name', lookup_expr='icontains')

    class Meta:
        model = CashOut
        fields = ('cash_date_release__month', 'name')


class TimeSheetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSheetSerializer
    filter_class = (TimeSheetFilter)

    def get_queryset(self):
        timesheet = TimeSheet.objects.all()
        is_staff = self.request.user.is_staffs
        is_client = self.request.user.is_client
        is_superuser = self.request.user.is_superuser
        current_year = datetime.date.today().year
        year = Q(shift_date__year=current_year)

        if is_client:
            client = Q(
                clients_full_name__full_name__icontains=self.request.user.clients.full_name)
            queryset = timesheet.filter(client & Q(
                admin_approval="Approved") & Q(status="Approved"))
            return queryset
        elif is_staff:
            staff = Q(
                assigned_approval__full_name__icontains=self.request.user.staffs)
            qs = timesheet.filter(staff & year)
            return qs
        elif is_superuser and is_client:
            qs = TimeSheet.objects.all()
            return qs


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
        elif self.request.user.is_superuser:
            qs = PaymentMade.objects.all()
            return qs


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
        elif self.request.user.is_superuser:
            qs = CashOut.objects.all()
            return qs
