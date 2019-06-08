from django.shortcuts import render

from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .serializers import AffordableLandSerializer, FranklinSerializer

from .models import (
    AffordableLandInvestment, 
    AffordableLandSpiels,
    FranklinManagement,
    FranklinSpiels,
    )


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AffordableLandView(LoginRequiredMixin, TemplateView):
    template_name = "callme/affordableland/landinvestment.html"
    model = AffordableLandInvestment

    def get(self, request, *args, **kwargs):
        spiels = AffordableLandSpiels.objects.all()
        context = {
            'spiels': spiels,
        }
        return render(request, self.template_name, context)


class AffordableLandViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = (AffordableLandSerializer)

    def get_queryset(self):
        queryset = AffordableLandInvestment.objects.all()
        return queryset


class FranklinManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/franklinmanagement/franklinmanagement.html'
    
    def get(self, request, *args, **kwargs):
        spiels = FranklinSpiels.objects.all()
        context = {
            'spiels': spiels,
        }
        return render(request, self.template_name, context)


class FranklinManagementViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = (FranklinSerializer)

    def get_queryset(self):
        queryset = FranklinManagement.objects.all()
        return queryset
