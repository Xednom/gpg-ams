from django.urls import path

from . import views

app_name="masterboard"
urlpatterns=[
    path('view-masterboard', views.MasterBoardView.as_view(), name='view_masterboard'),
    path('add-masterboard', views.AddMasterBoardView.as_view(), name='add_masterboard')
]
