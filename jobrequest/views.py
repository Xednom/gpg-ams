from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import JobRequest, StatusOfTheJobRequest
from .serializers import JobRequestSerializer, StatusOfTheJobRequestSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class JobRequestView(LoginRequiredMixin, ListView):
    model = JobRequest
    template_name = 'jobrequest/jobrequest.html'
    paginate_by = 1
    ordering = '-date'
    context_object_name = 'jobs'


class UpdateJobRequest(LoginRequiredMixin, ListView):
    model = JobRequest
    template_name = 'jobrequest/jobrequest.html'


class StatusOfTheJobRequestViewSet(viewsets.ModelViewSet):
    queryset = StatusOfTheJobRequest.objects.all()
    serializer_class = StatusOfTheJobRequestSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('type_of_status',)


class JobRequestViewSet(viewsets.ModelViewSet):
    queryset = JobRequest.objects.all()
    serializer_class = JobRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_code', 'VA_admin_support')
