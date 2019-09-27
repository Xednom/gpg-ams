from django.shortcuts import render

from django_filters import CharFilter, DateFilter
from django_filters.rest_framework import FilterSet
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import LandAcademyInventory, O20SmartPricing
from .serializers import LandAcademySerializer, SmartPricingSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class LandAcademyView(LoginRequiredMixin, TemplateView):
    template_name = 'landacademy/inventory/view_inventory.html'


class AddLandAcademyView(LoginRequiredMixin, AccessMixin, TemplateView):
    template_name = 'landacademy/inventory/add_inventory.html'


class SmartPricingView(LoginRequiredMixin, TemplateView):
    template_name = 'landacademy/smartpricing/view_pricing.html'


class AddSmartPricingView(LoginRequiredMixin, TemplateView):
    template_name = 'landacademy/smartpricing/add_pricing.html'


class InventoryFilterSet(FilterSet):
    date_requested = DateFilter(field_name='date_requested', lookup_expr='contains')
    date_completed = DateFilter(field_name='date_completed', lookup_expr='contains')
    date_payment_made = DateFilter(field_name='date_payment_made', lookup_expr='contains')
    client = CharFilter(field_name='client', lookup_expr='icontains')
    status_of_order = CharFilter(field_name='status_of_order', lookup_expr='contains')
    payment_status = CharFilter(field_name='payment_status', lookup_expr='contains')
    order_name = CharFilter(field_name='order_name', lookup_expr='icontains')

    class Meta:
        model = LandAcademyInventory
        fields = ('date_requested', 'date_completed',
                  'date_payment_made', 'client', 'status_of_order', 'payment_status', 'order_name')


class SmartPricingFilterSet(FilterSet):
    date_completed = DateFilter(field_name='date_completed', lookup_expr='icontains')
    client = CharFilter(field_name='client__full_name', lookup_expr='icontains')
    virtual_assistant = CharFilter(field_name='virtual_assistant__full_name', lookup_expr='icontains')

    class Meta:
        model = O20SmartPricing
        fields = ('date_completed', 'client', 'virtual_assistant')


class LandAcademyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LandAcademySerializer
    filter_class = (InventoryFilterSet)

    def get_queryset(self):
        land_academy_data = LandAcademyInventory.objects.all()
        return land_academy_data


class SmartPricingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SmartPricingSerializer
    filter_class = (SmartPricingFilterSet)

    def get_queryset(self):
        qs = O20SmartPricing.objects.all()
        return qs
