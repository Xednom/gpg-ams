from django.urls import path

from . import views

app_name="landacademy"
urlpatterns = [
    path('add-land-academy-inventory', views.AddLandAcademyView.as_view(), name="add_landacademy"),
    path('view-land-academy-inventory', views.LandAcademyView.as_view(), name="view_landacademy"),
]