from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
        Client,
        CompanyName,
        ProjectManager,
        TypeOfTask,
        SeniorManager,
    )
from .serializers import (
            ClientSerializer,
            ClientNameSerializer,
            ProjectManagerSerializer,
            TypeOfTaskSerializer,
            SeniorManagerSerializer,
            CustomUserSerializer
        )
from fillables.models import VirtualAssistant

from landmaster.serializers import VaSerializer

from django.shortcuts import render
from django.views.generic import View, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SeniorManagerView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/seniors_tab.html'


class ProjectManagerView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/project_manager.html'
    context_object_name = 'all_assigned_job'

    def get_context_data(self, **kwargs):
        context = super(ProjectManagerView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        user = self.request.user
        queryset = Client.objects.filter(
            clients_project_manager__project_manager=user)
        return queryset


class ClientNameViewSet(viewsets.ModelViewSet):
    queryset = CompanyName.objects.all()
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


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class VirtualAssistantViewSet(viewsets.ModelViewSet):
    queryset = VirtualAssistant.objects.all()
    serializer_class = VaSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('VA_assigned__full_name', 'client_code')

    def get_queryset(self):
        user = self.request.user
        queryset = Client.objects.filter(
            senior_manager__name=user, status="Active")
        return queryset
