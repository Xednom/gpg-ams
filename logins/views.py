from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginsSerializer

from .models import Logins


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class LoginsView(LoginRequiredMixin, TemplateView):
    template_name = 'logins/list_logins.html'


class LoginsViewSet(viewsets.ModelViewSet):
    serializer_class = LoginsSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.staffs.full_name
        qs = Logins.objects.filter(give_access_to__name=user)
        return qs
