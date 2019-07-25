import datetime
import django_filters

from django.shortcuts import render


from django_filters.rest_framework import FilterSet
from django_filters import DateRangeFilter, DateFilter, CharFilter, NumberFilter
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import TimeSheet, PaymentMade
from .serializers import TimeSheetSerializer, PaymentMadeSerializer, CashOutSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class VaTimeSheetView(TemplateView):
    template_name = 'timesheet/va_timesheet.html'


class TimeSheetView(TemplateView):
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
        model = PaymentMade
        fields = ('cash_date_release__month', 'name')


class TimeSheetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSheetSerializer
    filter_class = (TimeSheetFilter)

    def get_queryset(self):
        current_year = datetime.date.today().year
        if self.request.user.is_client:
            queryset = TimeSheet.objects.filter(Q(clients_full_name__full_name__icontains=self.request.user.clients.full_name) |
                                                Q(shift_date__year=current_year))
            return queryset
        elif self.request.user.is_staffs:
            queryset = TimeSheet.objects.filter(Q(assigned_va__full_name__icontains=self.request.user.staffs.full_name),
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
            queryset = PaymentMade.objects.filter(Q(name__full_name=self.request.user.staffs.full_name),
                                                  Q(cash_date_release__year=current_year))
            return queryset
