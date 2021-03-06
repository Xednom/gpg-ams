from django.shortcuts import render

from django_filters import CharFilter, ChoiceFilter
from django_filters.rest_framework import FilterSet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import inventory, VaForm
from .serializers import InventorySerializer, VaFormSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/inventory/view_inventory.html'


class VaFormView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/forms/view_forms.html'


class AddInventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/inventory/add_inventory.html'


class InventoryFilters(FilterSet):
    STATUS = (
        ('New', 'New'),
        ('Transferred to Podio - Personal Account', 'Transferred to Podio - Personal Account'),
        ('Transferred to Land Speed', 'Transferred to Land Speed'),
        ('Transferred to Investment Dominator', 'Transferred to Investment Dominator'),
        ('Airtable', 'Airtable'),
        ('Others', 'Others'),
    )
    client_full_name = CharFilter(field_name='client_full_name', lookup_expr='icontains')
    customer_representative = CharFilter(field_name='customer_representative', lookup_expr='icontains')
    type_of_form = CharFilter(field_name='type_of_form', lookup_expr='icontains')
    financial_status = CharFilter(field_name='financial_status', lookup_expr='contains')
    status = ChoiceFilter(choices=STATUS)
    lead_transferred_by = CharFilter(field_name='lead_transferred_by', lookup_expr='icontains')

    class Meta:
        model = inventory
        fields = ('client_full_name', 'type_of_form', 'financial_status',
                  'customer_representative', 'status', 'lead_transferred_by')


class CallMeInventoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializer
    filter_class = (InventoryFilters)

    def get_queryset(self):
        if self.request.user.is_staffs:
            queryset = inventory.objects.filter(customer_representative__icontains=self.request.user.staffs)
        elif self.request.user.is_client:
            queryset = inventory.objects.filter(client_full_name__icontains=self.request.user.clients)
        return queryset
    
    def perform_create(self, serializer):
        if self.request.user.is_staffs:
            return serializer.save(customer_representative=self.request.user.staffs)
            

class CallMeVaFormViewSet(viewsets.ModelViewSet):
    queryset = VaForm.objects.all()
    serializer_class = VaFormSerializer
    permission_classes = [IsAuthenticated]
