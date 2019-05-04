from django.urls import path

from . import views

app_name = 'landmaster'
urlpatterns = [
    path('due-diligence/', views.AddDueDiligenceView.as_view(), name='due_diligence'),
    path('add-due-diligence-tracking/', views.AddDueDiligenceTrackerView.as_view(), name='add_due_diligence_tracker'),
    path('view-due-diligence/', views.DueDiligenceView.as_view(), name='view_due_diligence'),
    path('view-due-diligence-tracking/', views.DueDiligenceTrackingView.as_view(), name='view_due_diligence_tracker')
]