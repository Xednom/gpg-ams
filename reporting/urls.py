from django.urls import path

from . import views

app_name = 'reporting'
urlpatterns = [
    path('reporting', views.ReportingView.as_view(), name='view_report'),
]
