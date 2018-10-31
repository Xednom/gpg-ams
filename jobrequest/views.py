from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import JobRequest
from .serializers import JobRequestSerializer


class JobRequestViewSet(viewsets.ModelViewSet):
    queryset = JobRequest.objects.all()
    serializer_class = JobRequestSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_code')
