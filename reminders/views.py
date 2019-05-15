import datetime

from django.shortcuts import render

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
    search_fields = ('manager_under',)

    def get_queryset(self):
        current_date = datetime.date.today().year
        queryset = ManagerReminders.objects.filter(Q(date__year=current_date), 
                                                   Q(manager_under=self.request.user.staffs.full_name))
        return queryset

