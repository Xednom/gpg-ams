from rest_framework import routers
from client.views import ClientViewSet
from jobrequest.views import JobRequestViewSet
from reporting.views import ReportingViewSet


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet)
router.register(r'jobrequest', JobRequestViewSet)
router.register(r'reporting', ReportingViewSet)
