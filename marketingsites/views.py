from django.shortcuts import render

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


class InventoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializers

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
            return serializer.save(marketing_associate=self.request.user.staffs.company_name)