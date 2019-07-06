import datetime

from django.shortcuts import render
from django.db.models import Q

from django_filters import DateFilter, NumberFilter
from django_filters.rest_framework import FilterSet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import FinancialReport
from .serializers import FinancialReportSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class FinancialReportView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/financialreport/view_financial.html'


class MinutesReportView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/financialreport/view_minutes_inventory.html'


class FinancialFilters(FilterSet):
    date__month = NumberFilter(field_name='date_created', lookup_expr='month')

    class Meta:
        model = FinancialReport
        fields = ('date__month',)


class FinancialViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FinancialReportSerializer
    filter_class = (FinancialFilters)
    filterset_fields = ('date_created',)

    def get_queryset(self):
        current_year = datetime.date.today().year
        qs = FinancialReport.objects.filter(Q(client_full_name__full_name=self.request.user.clients.full_name), 
        Q(date_created__year=current_year))
        return qs
