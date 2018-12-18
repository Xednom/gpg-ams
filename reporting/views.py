from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import viewsets, filters
from .models import VATimeSheet
from .serializers import VATimeSheetSerializer


class ReportingView(ListView):
    model = VATimeSheet
    template_name = 'reporting/reporting.html'
    paginated_by = 10


class ReportingViewSet(viewsets.ModelViewSet):
    queryset = VATimeSheet.objects.all()
    serializer_class = VATimeSheetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title_of_job_request')
