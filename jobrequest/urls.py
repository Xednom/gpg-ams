from django.urls import path

from . import views

app_name = 'jobrequest'
urlpatterns = [
    path('add-job-request/', views.JobRequestView.as_view(), name="add_job_request"),
    path('add-time-sheet/', views.JobRequestTimeSheet.as_view(), name="add_time_sheet"),
    path('update-job-request/', views.UpdateJobRequestView.as_view(), name="update_job_request"),
    path('view-time-sheet/', views.TimeSheetView.as_view(), name="view_time_sheet")
]
