from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('senior-tab/', views.ClientView.as_view(), name="seniors_tab"),
]
