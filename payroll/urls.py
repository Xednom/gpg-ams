from django.urls import path

from . import views

app_name="payroll"
urlpatterns = [
    path('payroll/', views.PayrollView.as_view(), name='view_payroll'),
    path('add-payroll/', views.AddPayroll.as_view(), name='add_payroll')
]