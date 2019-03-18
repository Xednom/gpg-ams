from rest_framework import routers
from client.views import (
            ClientViewSet,
            ClientNameViewSet,
            ProjectManagerViewSet,
            TypeOfTaskViewSet,
            SeniorManagerViewSet,
            CustomUserViewSet
        )
from landmaster.views import DueDiligenceViewSet

from jobrequest.views import JobRequestViewSet, JobRequestTitleViewSet
from reporting.views import ReportingViewSet


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet, base_name="Client")
router.register(r'client-name', ClientNameViewSet)
router.register(r'project-manager', ProjectManagerViewSet)
router.register(r'type-of-task', TypeOfTaskViewSet)
router.register(r'senior-manager', SeniorManagerViewSet)
router.register(r'custom-user', CustomUserViewSet)
router.register(r'jobrequest', JobRequestViewSet)
router.register(r'job-request-title', JobRequestTitleViewSet)
router.register(r'reporting', ReportingViewSet)
router.register(r'due-diligence', DueDiligenceViewSet)