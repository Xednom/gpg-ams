from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('', views.LoginView.as_view(), name="login"),
    path('', views.LogoutView.as_view(), name="logout"),
]
