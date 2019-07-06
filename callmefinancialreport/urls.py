from django.urls import path

from . import views

app_name='callmefinancialreport'
urlpatterns = [
    path('payment-made/', views.FinancialReportView.as_view(), name="view_financial"),
    path('minutes-inventory/', views.MinutesReportView.as_view(), name="view_minutes")
]
