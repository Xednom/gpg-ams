import datetime

from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

from django_filters.rest_framework import FilterSet
from django_filters import DateFilter, CharFilter, NumberFilter

from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import ManagerReminders
from users.models import Clients, Staffs
from .serializers import ReminderSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ReminderView(LoginRequiredMixin, ListView):
    template_name = 'reminder/reminder.html'
    model = ManagerReminders

    def get(self, request, *args, **kwargs):
        reminders = ManagerReminders.objects.all()
        if self.request.user.is_client:
            requestee_reminders = reminders.filter(Q(requestee__icontains=self.request.user.clients.full_name))
            requestor_reminders = reminders.filter(Q(requestor__icontains=self.request.user.clients.full_name))
        elif self.request.user.is_staffs:
            requestee_reminders = reminders.filter(Q(requestee__icontains=self.request.user.staffs.full_name))
            requestor_reminders = reminders.filter(Q(requestor__icontains=self.request.user.staffs.full_name))
        context = {
            'requestee_reminders': requestee_reminders,
            'requestor_reminders': requestor_reminders
        }
        return render(request, self.template_name, context)


class AddReminder(LoginRequiredMixin, TemplateView):
    template_name = 'reminder/add_reminder.html'


class ReminderFilters(FilterSet):
    date__month = NumberFilter(field_name='date', lookup_expr='icontains')
    status = CharFilter(field_name='status', lookup_expr='icontains')
    name = CharFilter(field_name='requestor', lookup_expr='icontains')

    class Meta:
        model = ManagerReminders
        fields = ('date__month', 'status', 'name')


class ReminderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReminderSerializer
    filter_class = (ReminderFilters)
    search_fields = ('requestor',)

    def get_queryset(self):
        current_date = datetime.date.today().year
        current_month =datetime.date.today().month
        if self.request.user.is_client:
            queryset = ManagerReminders.objects.filter(Q(date__year=current_date),
            Q(date__month=current_month),
            Q(requestor=self.request.user.clients.full_name) |
            Q(requestee=self.request.user.clients.full_name))
        elif self.request.user.is_staffs:
            queryset = ManagerReminders.objects.filter(Q(date__year=current_date),
            Q(date__month=current_month),
            Q(requestee=self.request.user.staffs.full_name) |
            Q(requestor=self.request.user.staffs.full_name))
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_staffs:
            return serializer.save(requestor=self.request.user.staffs.full_name)
        elif self.request.user.is_client:
            return serializer.save(requestor=self.request.user.clients.full_name)


