from django.urls import path

from . import views

app_name="marketing_inventory"
urlpatterns = [
    path('view-marketing-sites-inventory/', views.InventoryView.as_view(), name='view_inventory'),
    path('add-marketing-sites-inventory/', views.AddInventoryView.as_view(), name='add_inventory'),
]