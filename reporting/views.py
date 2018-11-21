from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import viewsets, filters
from .models import Report
from .serializers import ReportingSerializer


class ReportingView(ListView):
    model = Report
    template_name = 'reporting/reporting.html'
    paginated_by = 10


class ReportingViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title_of_job_request')
