from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.paginator import Paginator

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import JobRequest
from fillables.models import JobTitleRequest
from .serializers import JobRequestSerializer, JobTitleRequestSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class JobRequestView(LoginRequiredMixin, ListView):
    model = JobRequest
    template_name = 'jobrequest/jobrequest.html'
    paginate_by = 1
    ordering = '-date'
    context_object_name = 'jobs'


class UpdateJobRequestView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = JobRequest
    permission_required = ('jobrequest.view_jobrequest',)
    template_name = 'jobrequest/update_job_request.html'


class JobRequestViewSet(viewsets.ModelViewSet):
    queryset = JobRequest.objects.all()
    serializer_class = JobRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('date', 'client_code', 'VA_admin_support')


class JobRequestTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitleRequest.objects.all()
    serializer_class = JobTitleRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
