from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
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


class CallMeInventoryViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = InventorySerializer

    def get_queryset(self):
        if self.request.user.is_staffs:
            queryset = inventory.objects.all()
        elif self.request.user.is_client:
            queryset = inventory.objects.filter(client_full_name=self.request.user.clients.full_name)
        return queryset
