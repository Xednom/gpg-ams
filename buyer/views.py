from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import CustomerCareSerializer

from .models import CustomerCareSpecialist

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CustomerCareViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = (CustomerCareSerializer)

    def get_queryset(self):
        queryset = CustomerCareSpecialist.objects.all()
        return queryset
