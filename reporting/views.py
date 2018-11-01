from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Report
from .serializers import ReportingSerializer


class ReportingViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title_of_job_request')
