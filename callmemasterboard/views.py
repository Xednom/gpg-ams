from django.shortcuts import render


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


class MasterBoardView(TemplateView):
    template_name = 'callme/masterboard/view_masterboard.html'


class AddMasterBoardView(TemplateView):
    template_name = 'callme/masterboard/add_masterboard.html'


class MasterBoardViewSets(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = MasterBoardSerializer

    def get_queryset(self):
        if self.request.user.is_staffs:
            queryset = MasterBoard.objects.all()
        elif self.request.user.is_client:
            queryset = MasterBoard.objects.filter(
                client_name=self.request.user.clients.full_name)
        return queryset
