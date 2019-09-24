from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from .models import AdsContent
from .serializers import AdsSerializer

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdsViewSet(viewsets.ModelViewSet):
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ads_list = AdsContent.objects.all()
        if self.request.user.is_client:
            qs = ads_list.filter(client=self.request.user.clients)
            return qs
        elif self.request.user.is_staffs:
            qs = ads_list.filter(ads_writer=self.request.user.staffs)
            return qs