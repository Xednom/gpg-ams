from django.urls import path

from . import views

app_name='logins'
urlpatterns = [
    path('list-of-logins/', views.LoginsView.as_view(), name='login')
]