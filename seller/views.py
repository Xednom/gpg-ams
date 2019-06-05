from django.shortcuts import render

from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .serializers import AffordableLandSerializer

from .models import AffordaleLandInvestment, AffordableLandSpiels


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AffordableLandView(LoginRequiredMixin, TemplateView):
    template_name = "callme/affordableland/landinvestment.html"
    model = AffordableLandSpiels

    def get(self, request, *args, **kwargs):
        spiels = AffordableLandSpiels.objects.all()
        context = {
            'spiels': spiels,
        }
        return render(request, self.template_name, context)


class AffordableLandViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = (AffordableLandSerializer)

    def get_queryset(self):
        queryset = AffordaleLandInvestment.objects.all()
        return queryset
