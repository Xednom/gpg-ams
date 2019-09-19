from django.urls import path

from . import views

app_name="callmeinventory"
urlpatterns = [
    path('view-inventory', views.InventoryView.as_view(), name='view_inventory'),
    path('add-inventory', views.AddInventoryView.as_view(), name='add_inventory'),
    path('view-va-forms', views.VaFormView.as_view(), name='view_forms')
]
