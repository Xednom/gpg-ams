from django.urls import path

from . import views

app_name="payroll"
urlpatterns = [
    path('payroll/', views.AddPayrollView.as_view(), name='add_payroll')
]