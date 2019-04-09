from django import template
from django.db.models import Q

from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DueDiligence

from .serializers import DueDiligenceSerializer

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


class DueDiligenceView(LoginRequiredMixin, TemplateView):
    template_name = 'landmaster/view_due_diligence.html'


class DueDiligenceViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permistion_classes = (IsAuthenticated,)
    serializer_class = DueDiligenceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = DueDiligence.objects.filter(Q(company_owner=user) | Q(project_manager__project_manager=user))
        return queryset

    def perform_create(self, serializer):
        return serializer.save(company_name=self.request.user.clients.company_name)
