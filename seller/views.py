from django.shortcuts import render

from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin