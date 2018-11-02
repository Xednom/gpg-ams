from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, filters
from .models import Client
from .serializers import ClientSerializer


class ClientView(LoginRequiredMixin, View):
    template_name = 'client/seniors_tab.html'

    def get(self, request):
        return render(request, self.template_name)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('clients_code')
