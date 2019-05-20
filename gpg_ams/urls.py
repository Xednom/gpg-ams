"""gpg_ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications.urls
from django.contrib import admin
from django.urls import path, include

from .routers import router

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('users.urls')),
    path('client/', include('client.urls')),
    path('logins/', include('logins.urls')),
    path('land-master/', include('landmaster.urls')),
    path('jobrequest/', include('jobrequest.urls')),
    path('payroll/', include('payroll.urls')),
    path('timesheet/', include('clienttimesheet.urls')),
    path('reporting/', include('reporting.urls')),
    path('inbox/notifications', include(notifications.urls, namespace='notifications'))
]

admin.site.site_title = "GPG site admin"
admin.site.site_header = "GPG Administration"
