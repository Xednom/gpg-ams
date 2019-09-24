from django.urls import path

from . import views

app_name='ads'
urlpatterns = [
    path('view-ads', views.AdsView.as_view(), name="view-ads"),
    path('add-ads', views.AddAdsView.as_view(), name="add-ads")
]
