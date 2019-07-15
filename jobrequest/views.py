from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.paginator import Paginator
from django.db.models import Q

from django.urls import reverse_lazy

from django.utils.timezone import now

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import (
    JobRequest, 
    JobRequestTimeSheet as jst
    )
from fillables.models import JobTitleRequest
from .serializers import (
        JobRequestSerializer, JobTitleRequestSerializer,
        TimeSheetSerializer
    )


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


class TimeSheetView(LoginRequiredMixin, ListView):
    model = jst
    template_name = 'jobrequest/view_timesheet.html'


class JobRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JobRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('date', 'client_code', 'VA_admin_support')

    def get_queryset(self):
        #  data will only show by company name.
        is_staff = self.request.user.staffs
        is_client = self.request.user.is_client
        job_request = JobRequest.objects.all()
        
        if is_client:
            queryset = job_request.filter(Q(requestors_name=self.request.user.clients.full_name))
            return queryset
        elif is_staff:
            if self.request.user.staffs.position == 'Project Managers':
                    queryset = job_request.filter(Q(assigned_project_managers__full_name__icontains=self.request.user.staffs.full_name) |
                                                  Q(assigned_va__full_name__icontains=self.request.user.staffs.full_name),)
                    return queryset
            elif self.request.user.staffs.position == 'General Administrative Support':
                if is_staff:
                    queryset = job_request.filter(Q(assigned_va__full_name__icontains=self.request.user.staffs.full_name),
                                                  Q(assigned_project_managers__full_name__icontains=self.request.user.staffs.full_name))
                    return queryset

    def perform_create(self, serializer):
        is_staff = self.request.user.is_staff
        is_client = self.request.user.is_client
        if is_client:
            return serializer.save(requestors_name=self.request.user.clients.full_name, 
            company_name=self.request.user.clients.company_name)
        elif is_staff:
            return serializer.save(requestors_name=self.request.user.staffs.full_name)


class JobRequestTitleViewSet(viewsets.ModelViewSet):
    queryset = JobRequest.objects.all()
    serializer_class = JobTitleRequestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class JobRequestTimeSheet(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'jobrequest/add_timesheet.html'
    model = jst
    fields = [
        'job_title', 'staff', 'client', 'time_in', 'time_out', 'notes'
    ]
    success_message = "Successfully added a time sheet!"

    def form_valid(self, form):
        form.instance.staff__full_name = self.request.user.staffs.full_name
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("jobrequest:add_time_sheet")


class JobRequestTimeSheetViewSet(viewsets.ModelViewSet):
    serializer_class = TimeSheetSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        time_sheet = jst.objects.all()
        if self.request.user.is_client:
            qs = time_sheet.filter(Q(client__full_name=self.request.user.clients.full_name))
            return qs
        elif self.request.user.is_staffs:
            qs = time_sheet.filter(Q(staff__full_name=self.request.user.staffs.full_name))
            return qs
