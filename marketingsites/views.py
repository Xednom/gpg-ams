from django.shortcuts import render

from django_filters import DateFilter, CharFilter
from django_filters.rest_framework import FilterSet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import Inventory
from .serializers import InventorySerializers


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'marketing/view_marketing.html'


class AddInventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'marketing/add_marketing.html'


class InventoryFilterSet(FilterSet):
    date_requested = DateFilter(field_name='date_requested', lookup_expr='icontains')
    date_completed = DateFilter(field_name='date_completed', lookup_expr='icontains')
    type_of_marketing_sites = CharFilter(field_name='type_of_marketing_sites', lookup_expr='contains')
    client_full_name = CharFilter(field_name='client_full_name', lookup_expr='icontains')
    client_company_name = CharFilter(field_name='client_company_name', lookup_expr='icontains')
    apn = CharFilter(field_name='apn', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='contains')
    post_for_approval = CharFilter(field_name='post_for_approval', lookup_expr='contains')

    class Meta:
        model = Inventory
        fields = ('date_requested', 'date_completed',
                  'type_of_marketing_sites', 'client_full_name', 'client_company_name',
                  'apn', 'status', 'post_for_approval')


class InventoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializers
    filter_class = (InventoryFilterSet)

    def get_queryset(self):
        is_staff = self.request.user.is_staffs
        is_client = self.request.user.is_client
        if is_staff:
            queryset = Inventory.objects.filter(Q(marketing_associate__icontains=self.request.user.staffs.full_name))
        elif is_client:
            queryset = Inventory.objects.filter(Q(client_full_name__icontains=self.request.user.clients.full_name))
        return queryset
    
    def perform_create(self, serializer):
        is_staff = self.request.user.is_staffs
        is_client = self.request.user.is_client
        if is_client:
            return serializer.save(client_full_name=self.request.user.clients.full_name,
            client_company_name=self.request.user.clients.company_name)
        elif is_staff:
            return serializer.save(marketing_associate=self.request.user.staffs.full_name)
