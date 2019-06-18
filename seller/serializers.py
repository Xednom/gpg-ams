import datetime

from django.db.models import Q, Sum
from rest_framework import serializers

from .models import AffordableLandInvestment, FranklinManagement
from buyer.models import CustomerCareSpecialist