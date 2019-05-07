from django import template
from django.db.models import Q

from django.views.generic import View, ListView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DueDiligence, DueDiligencesCleared

from .serializers import DueDiligenceSerializer, DueDiligenceClearedSerializer

register = template.Library()


@register.filter(name='Client')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
        

class AddDueDiligenceView(LoginRequiredMixin, ListView):
    model = DueDiligence
    template_name = 'landmaster/due_diligence.html'


class AddDueDiligenceTrackerView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'landmaster/due_diligence_tracking.html'
    model = DueDiligencesCleared
    fields = ['date_of_call', 'client_full_name',
              'client_company_name', 'apn', 'call_in', 'call_out',
              'department_calling_about', 'contact_number', 'operators_details',
              'notes']
    success_message = "Successfully added Due Diligence Tracking Information."

    def form_valid(self, form):
        form.instance.customer_service_representative = self.request.user.staffs.full_name
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("landmaster:add_due_diligence_tracker")

class DueDiligenceTrackingView(TemplateView):
    template_name = 'landmaster/view_dd_tracking.html'


class DueDiligenceView(LoginRequiredMixin, TemplateView):
    template_name = 'landmaster/view_due_diligence.html'


class DueDiligenceViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = DueDiligenceSerializer

    def get_queryset(self):
        user = self.request.user.staffs.position
        queryset = DueDiligence.objects.filter(Q(company_owner_or_requestor=self.request.user.clients.full_name) |
                                               Q(dd_team_assigned_va__name=self.request.user.staffs.full_name) | 
                                               Q(project_manager__project_manager=self.request.user.staffs.full_name))
        if user == 'Project Managers':
            queryset = DueDiligence.objects.filter(Q(project_manager__project_manager=self.request.user.staffs.full_name),
                                                   Q(status_of_dd="Sent to Project Manager") |
                                                   Q(status_of_dd="Project Managers Review") |
                                                   Q(status_of_dd="Sent to VA") |
                                                   Q(status_of_dd="VA Processing") |
                                                   Q(status_of_dd="Sent to Quality Specialist"))
        elif user == 'General Administrative Support':
            queryset = DueDiligence.objects.filter(Q(dd_team_assigned_va__name=self.request.user.staffs.full_name),
                                                   Q(status_of_dd="Sent to Project Manager") |
                                                   Q(status_of_dd="Project Managers Review") |
                                                   Q(status_of_dd="Sent to VA") |
                                                   Q(status_of_dd="VA Processing") |
                                                   Q(status_of_dd="Sent to Quality Specialist"))
        return queryset

    def perform_create(self, serializer):
        return serializer.save(company_name=self.request.user.clients.company_name)


class DueDiligenceTrackerViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = (DueDiligenceClearedSerializer)

    def get_queryset(self):
        queryset = DueDiligencesCleared.objects.filter(Q(client_full_name=self.request.user.clients.full_name) |
                                                       Q(client_company_name=self.request.user.clients.company_name) |
                                                       Q(customer_service_representative=self.request.user.staffs.full_name))
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(customer_service_representative=self.request.user.staffs.full_name)
