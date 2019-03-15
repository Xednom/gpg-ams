from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    DueDiligence,
    LandData,
    AdditionalLandInfo,
    CountyData,
    TaxData,
    ZoningData,
    DataOnUtilities,
)

from .serializers import (
    DueDiligenceSerializer,
    LandDataSerializer,
    AdditionalLandInfoSerializer,
    CountyDataSerializer,
    TaxDataSerializer,
    ZoningDataSerializer,
    DataOnUtilitiesSerializer,
)


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
        

class DueDiligenceView(LoginRequiredMixin, ListView):
    model = DueDiligence
    template_name = 'landmaster/due_diligence.html'


class DueDiligenceViewSet(viewsets.ModelViewSet):
    queryset = DueDiligence.objects.all()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permistion_classes = (IsAuthenticated,)
    serializer_class = DueDiligenceSerializer


class LandDataViewSet(viewsets.ModelViewSet):
    queryset = LandData.objects.all()
    serializer_class = LandDataSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    

class AdditionalLandInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionalLandInfo.objects.all()
    serializer_class = AdditionalLandInfoSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class CountyDataViewSet(viewsets.ModelViewSet):
    queryset = CountyData.objects.all()
    serializer_class = CountyDataSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class TaxDataViewSet(viewsets.ModelViewSet):
    queryset = TaxData.objects.all()
    serializer_class = TaxDataSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class ZoningDataViewSet(viewsets.ModelViewSet):
    queryset = ZoningData.objects.all()
    serializer_class = ZoningDataSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class DataOnUtilitiesViewSet(viewsets.ModelViewSet):
    queryset = DataOnUtilities.objects.all()
    serializer_class = DataOnUtilitiesSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)