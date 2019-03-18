from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DueDiligence

from .serializers import DueDiligenceSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
        

class DueDiligenceView(LoginRequiredMixin, ListView):
    model = DueDiligence
    template_name = 'landmaster/due_diligence.html'


class DueDiligenceViewSet(viewsets.ModelViewSet):
    queryset = DueDiligence.objects.all()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permistion_classes = (IsAuthenticated,)
    serializer_class = DueDiligenceSerializer