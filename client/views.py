from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
        Client,
        ClientLeadSource
    )
from .serializers import LeadSerializer
from fillables.models import VirtualAssistant

from landmaster.serializers import VaSerializer

from django.shortcuts import render
from django.views.generic import View, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User=get_user_model()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SeniorManagerView(LoginRequiredMixin, ListView):
    model=Client
    template_name='client/seniors_tab.html'


class LeadView(LoginRequiredMixin, ListView):
    model = ClientLeadSource
    template_name = 'client/leads/view_leads.html'


class AddLeadView(LoginRequiredMixin, ListView):
    model = ClientLeadSource
    template_name = 'client/leads/add_leads.html'

class ProjectManagerView(LoginRequiredMixin, ListView):
    model=Client
    template_name='client/project_manager.html'
    context_object_name='all_assigned_job'

    def get_context_data(self, **kwargs):
        context=super(ProjectManagerView, self).get_context_data(**kwargs)
        context['count']=self.get_queryset().count()
        return context

    def get_queryset(self):
        user=self.request.user
        queryset=Client.objects.filter(
            clients_project_manager__project_manager=user)
        return queryset


class VirtualAssistantViewSet(viewsets.ModelViewSet):
    queryset=VirtualAssistant.objects.all()
    serializer_class=VaSerializer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lead_list = ClientLeadSource.objects.all()
        if self.request.user.is_client:
            qs = lead_list.filter(client=self.request.user.clients)
            return qs
        elif self.request.user.is_staffs:
            qs = lead_list.filter(virtual_assistant=self.request.user.staffs)
            return qs
