from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import FinancialReport
from .serializers import FinancialReportSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class FinancialReportView(LoginRequiredMixin, TemplateView):
    template_name = 'callme/financialreport/view_financial.html'


class FinancialViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = FinancialReportSerializer

    def get_queryset(self):
        qs = FinancialReport.objects.filter(client_full_name__full_name=self.request.user.clients.full_name)
        return qs
