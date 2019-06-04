from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.paginator import Paginator
from django.db.models import Q


from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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


class UpdateJobRequestView(LoginRequiredMixin, ListView):
    model = JobRequest
    # permission_required = ('jobrequest.view_jobrequest',)
    template_name = 'jobrequest/update_job_request.html'


class JobRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JobRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('date', 'client_code', 'VA_admin_support')

    def get_queryset(self):
        #  data will only show by company name.
        position = self.request.user.staffs.position
        is_staff = self.request.user.staffs
        is_client = self.request.user.is_client
        if position == 'Project Managers':
            if is_staff:
                queryset = JobRequest.objects.filter(Q(assigned_project_managers__project_manager=self.request.user.staffs.full_name))
                return queryset
        elif position == 'General Administrative Support':
            if is_staff:
                queryset = JobRequest.objects.filter(Q(assigned_va__name=self.request.user.staffs.full_name))
                return queryset
        elif is_client:
            queryset = JobRequest.objects.filter(Q(requestors_name=self.request.user.clients.full_name))
            return queryset

    def perform_create(self, serializer):
        return serializer.save(requestors_name=self.request.user.clients.full_name, company_name=self.request.user.clients.company_name)


class JobRequestTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitleRequest.objects.all()
    serializer_class = JobTitleRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
