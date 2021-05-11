from django.urls import path

from . import views

app_name="timesheet"
urlpatterns = [
    path('your-timesheet/', views.TimeSheetView.as_view(), name='view_timesheet'),
    path('va-timesheet/', views.VaTimeSheetView.as_view(), name='va_timesheet'),
    # path('add-timesheet/', views.AddVaTimeSheetView.as_view(), name='add_timesheet'),
    path('masterboard-timesheet/', views.TimeSheetMasterView.as_view(), name='master_timesheet')
]
