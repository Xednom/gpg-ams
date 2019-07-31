from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('client-profile/', views.ClientsProfileView.as_view(), name="clients_profile"),
    path('staff-profile/', views.StaffsProfileView.as_view(), name="staffs_profile"),
    path('json-chart/client_status_data/', views.client_status_data, name='client_status_data'),
    path('json-chart/job_request_data/', views.job_request_status_data, name='job_request_status_data'),
]

handler404 = 'views.error_404_view'
