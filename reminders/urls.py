from django.urls import path

from . import views

app_name = 'reminders'
urlpatterns = [
    path('your-reminders/', views.ReminderView.as_view(), name="view-reminders"),
    path('add-your-reminders/', views.AddReminder.as_view(), name="add-reminders")
]
