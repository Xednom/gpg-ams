from django.urls import path

from . import views

app_name="seller"

urlpatterns = [
    path('affordable-land-investment/', views.AffordableLandView.as_view(), name='affordable-land'),
    path('franklin-management/', views.FranklinManagementView.as_view(), name='franklin-management')
]