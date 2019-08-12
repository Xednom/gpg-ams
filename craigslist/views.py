from django.shortcuts import render

from django_filters.rest_framework import FilterSet
from django_filters import DateRangeFilter, DateFilter, CharFilter

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import CraiglistInventory
from .serializers import CraigListSerializer


class CraigslistView(LoginRequiredMixin, TemplateView):
    template_name = 'craigslist/craigslist_view.html'


class CraigslistAddView(LoginRequiredMixin, TemplateView):
    template_name = 'craigslist/craigslist_add.html'


class CraigslistFilter(FilterSet):
    date = DateFilter(field_name='date', lookup_expr='icontains')
    client_name = CharFilter(field_name='client_name_company_name__full_name', lookup_expr='icontains')
    cl_admin_support = CharFilter(field_name='cl_admin_support__full_name', lookup_expr='icontains')

    class Meta:
        model = CraiglistInventory
        fields = ('date', 'client_name', 'cl_admin_support')


class CraigListViewSet(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    serializer_class = CraigListSerializer
    filter_class = (CraigslistFilter)

    def get_queryset(self):
        if self.request.user.is_client:
            qs = CraiglistInventory.objects.filter(client_name_company_name__full_name=self.request.user.clients.full_name)
            return qs
        elif self.request.user.is_staffs:
            qs = CraiglistInventory.objects.filter(cl_admin_support__full_name=self.request.user.staffs.full_name)
            return qs
    
    def perform_create(self, serializer):
        is_client = self.request.user.is_client
        is_staff = self.request.user.is_staffs

        if is_staff:
            return serializer.save(cl_admin_support=self.request.user.staffs.full_name)
        elif is_client: 
            return serializer.save(client_name_company_name=self.request.user.clients)

