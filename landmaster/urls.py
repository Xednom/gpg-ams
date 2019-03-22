from django.urls import path

from . import views

app_name = 'landmaster'
urlpatterns = [
    path('due-diligence/', views.AddDueDiligenceView.as_view(), name='due_diligence'),
    path('view-due-diligence/', views.DueDiligenceView.as_view(), name='view_due_diligence')
]