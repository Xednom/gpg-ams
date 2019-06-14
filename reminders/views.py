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
from .serializers import ReminderSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ReminderView(LoginRequiredMixin, ListView):
    template_name = 'reminder/reminder.html'
    model = ManagerReminders

    def get(self, request, *args, **kwargs):
        if self.request.user.is_client:
            clients_reminders = ManagerReminders.objects.filter(Q(requestee=self.request.user.clients.full_name) |
                                                                Q(requestor=self.request.user.clients.full_name))
            context = {
                'clients_reminders': clients_reminders
            }
            return render(request, self.template_name, context)
        elif self.request.user.is_staffs:
            staffs_reminders = ManagerReminders.objects.filter(Q(requestee=self.request.user.staffs.full_name) |
                                                               Q(requestor=self.request.user.staffs.full_name))
            context = {
                'staffs_reminders': staffs_reminders
            }
            return render(request, self.template_name, context)


class AddReminder(LoginRequiredMixin, TemplateView):
    template_name = 'reminder/add_reminder.html'


class ReminderFilters(FilterSet):
    date__month = NumberFilter(field_name='date', lookup_expr='icontains')
    name = CharFilter(field_name='manager_under', lookup_expr='icontains')

    class Meta:
        model = ManagerReminders
        fields = ('date__month', 'name')


class ReminderViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = ReminderSerializer
    filter_class = (ReminderFilters)
    search_fields = ('requestor',)

    def get_queryset(self):
        current_date = datetime.date.today().year
        if self.request.user.is_client:
            queryset = ManagerReminders.objects.filter(Q(date__year=current_date),
                                                       Q(requestee=self.request.user.clients.full_name) |
                                                       Q(requestor=self.request.user.clients.full_name))
            return queryset
        elif self.request.user.is_staffs:
            queryset = ManagerReminders.objects.filter(Q(date__year=current_date),
                                                       Q(requestee=self.request.user.staffs.full_name) |
                                                       Q(requestor=self.request.user.staffs.full_name))
            return queryset
    
    def perform_create(self, serializer):
        if self.request.user.is_staffs:
            return serializer.save(requestor=self.request.user.staffs.full_name)
        elif self.request.user.is_client:
            return serializer.save(requestor=self.request.user.clients.full_name)


