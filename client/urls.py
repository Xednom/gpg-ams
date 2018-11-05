from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('senior-tab/', views.SeniorManagerView.as_view(), name="seniors_tab"),
    path('manager-tab/', views.ProjectManagerView.as_view(), name="manager_tab"),
]
