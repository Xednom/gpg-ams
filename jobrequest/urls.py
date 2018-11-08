from django.urls import path

from . import views

app_name = 'jobrequest'
urlpatterns = [
    path('add-job-request/', views.JobRequestView.as_view(), name="add_job_request"),
]
