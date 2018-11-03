from rest_framework import viewsets, filters
from .models import (
        Client,
        ClientName,
        ProjectManager,
        TypeOfTask,
        SeniorManager,
        StatusChoice
    )
from .serializers import (
            ClientSerializer,
            ClientNameSerializer,
            ProjectManagerSerializer,
            TypeOfTaskSerializer,
            SeniorManagerSerializer,
            StatusChoiceSerializer,
            CustomUserSerializer
        )

from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class ClientView(LoginRequiredMixin, View):
    template_name = 'client/seniors_tab.html'

    def get(self, request):
        return render(request, self.template_name)


class ClientNameViewSet(viewsets.ModelViewSet):
    queryset = ClientName.objects.all()
    serializer_class = ClientNameSerializer


class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer


class TypeOfTaskViewSet(viewsets.ModelViewSet):
    queryset = TypeOfTask.objects.all()
    serializer_class = TypeOfTaskSerializer


class SeniorManagerViewSet(viewsets.ModelViewSet):
    queryset = SeniorManager.objects.all()
    serializer_class = SeniorManagerSerializer


class StatusChoiceViewSet(viewsets.ModelViewSet):
    queryset = StatusChoice.objects.all()
    serializer_class = StatusChoiceSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('clients_code')
