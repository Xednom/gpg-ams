from django.urls import path

from . import views

app_name="payroll"
urlpatterns = [
    path('payroll/', views.PayrollView.as_view(), name='view_payroll'),
    path('add-payroll/', views.AddPayroll.as_view(), name='add_payroll'),
    path('payroll-report.pdf/', views.PdfCurrentPayroll.as_view(), name='pdf_current_payroll'),
    path('payroll-previous-month-report.pdf/', views.PdfPreviousPayroll.as_view(), name='pdf_previous_payroll')
]
