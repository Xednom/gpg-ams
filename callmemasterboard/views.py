from django.shortcuts import render

from django_filters import CharFilter, DateFilter
from django_filters.rest_framework import FilterSet
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import MasterBoard
from .serializers import MasterBoardSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return # To not perform the csrf check previously happening


class MasterBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/masterboard/view_masterboard.html'


class AddMasterBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/masterboard/add_masterboard.html'


class MasterBoardFilters(FilterSet):
    date_started = DateFilter(field_name='date_started', lookup_expr='icontains')
    type_of_crm = CharFilter(field_name='type_of_crm', lookup_expr='icontains')
    type_of_voip = CharFilter(field_name='type_of_voip', lookup_expr='icontains')
    client_name = CharFilter(field_name='client_name', lookup_expr='icontains')
    url_buyer = CharFilter(field_name='url_buyer', lookup_expr='contains')
    url_seller = CharFilter(field_name='url_seller', lookup_expr='contains')
    url_property_management = CharFilter(field_name='url_property_management', lookup_expr='contains')
    general_calls = CharFilter(field_name='general_calls', lookup_expr='icontains')
    voicemail = CharFilter(field_name='voicemail', lookup_expr='icontains')

    class Meta:
        model = MasterBoard
        fields = ('date_started', 'type_of_crm', 'type_of_voip', 'client_name',
                  'url_buyer', 'url_seller', 'url_property_management', 'general_calls', 'voicemail')


class MasterBoardViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MasterBoardSerializer
    filter_class = (MasterBoardFilters)

    def get_queryset(self):
        if self.request.user.is_staffs:
            queryset = MasterBoard.objects.all()
            return queryset
        elif self.request.user.is_client:
            queryset = MasterBoard.objects.filter(client_name__full_name=self.request.user.clients.full_name)
            return queryset
