from django.urls import path

from . import views

app_name = 'reporting'
urlpatterns = [
    path('reporting-view', views.ReportingView.as_view(), name='view_report'),
]
