from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import JobRequest, StatusOfTheJobRequest
from .serializers import JobRequestSerializer, StatusOfTheJobRequestSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class JobRequestView(LoginRequiredMixin, View):
    template_name = 'jobrequest/jobrequest.html'

    def get(self, request):
        return render(request, self.template_name)


class StatusOfTheJobRequestViewSet(viewsets.ModelViewSet):
    queryset = StatusOfTheJobRequest.objects.all()
    serializer_class = StatusOfTheJobRequestSerializer


class JobRequestViewSet(viewsets.ModelViewSet):
    queryset = JobRequest.objects.all()
    serializer_class = JobRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_code',)
