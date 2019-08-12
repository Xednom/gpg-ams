from django.urls import path

from . import views

app_name='craigslist_inventory'
urlpatterns=[
    path('view-craigslist/', views.CraigslistView.as_view(), name="craigslist-view"),
    path('add-craigslist/', views.CraigslistAddView.as_view(), name="craigslist-add")
]