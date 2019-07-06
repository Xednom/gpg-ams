from django.urls import path

from . import views

app_name='callmefinancialreport'
urlpatterns = [
    path('report/', views.FinancialReportView.as_view(), name="view_financial")
]