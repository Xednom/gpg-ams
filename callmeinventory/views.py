from django.shortcuts import render

from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import inventory
from .serializers import InventorySerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/inventory/view_inventory.html'


class AddInventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/inventory/add_inventory.html'


class InventoryFilters(FilterSet):
    client_full_name = CharFilter(field_name='client_full_name', lookup_expr='icontains')
    client_company_name = CharFilter(field_name='client_company_name', lookup_expr='icontains')
    customer_representative = CharFilter(field_name='customer_representative', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='icontains')
    lead_transferred_by = CharFilter(field_name='lead_transferred_by', lookup_expr='icontains')

    class Meta:
        model = inventory
        fields = ('client_full_name', 'client_company_name',
                  'customer_representative', 'status', 'lead_transferred_by')


class CallMeInventoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializer
    filter_class = (InventoryFilters)

    def get_queryset(self):
        if self.request.user.is_staffs:
            queryset = inventory.objects.all()
        elif self.request.user.is_client:
            queryset = inventory.objects.filter(client_full_name=self.request.user.clients.full_name)
        return queryset
