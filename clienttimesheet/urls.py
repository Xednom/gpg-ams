from django.urls import path

from . import views

app_name="timesheet"
urlpatterns = [
    path('your-timesheet/', views.TimeSheetView.as_view(), name='view_timesheet'),
    path('your-timesheet/', views.VaTimeSheetView.as_view(), name='va_timesheet')
]
