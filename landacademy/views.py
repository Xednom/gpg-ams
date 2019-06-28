from django.shortcuts import render

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


class LandAcademyViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = LandAcademySerializer

    def get_queryset(self):
        land_academy_data = LandAcademyInventory.objects.all()
        return land_academy_data


class SmartPricingViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = SmartPricingSerializer

    def get_queryset(self):
        qs = O20SmartPricing.objects.all()
        return qs
