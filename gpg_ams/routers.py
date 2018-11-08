from rest_framework import routers
from client.views import (
            ClientViewSet,
            ClientNameViewSet,
            ProjectManagerViewSet,
            TypeOfTaskViewSet,
            SeniorManagerViewSet,
            StatusChoiceViewSet,
            CustomUserViewSet
        )
from jobrequest.views import JobRequestViewSet, StatusOfTheJobRequestViewSet
from reporting.views import ReportingViewSet


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet, base_name="Client"),
router.register(r'client-name', ClientNameViewSet)
router.register(r'project-manager', ProjectManagerViewSet)
router.register(r'type-of-task', TypeOfTaskViewSet)
router.register(r'senior-manager', SeniorManagerViewSet)
router.register(r'status-choice', StatusChoiceViewSet)
router.register(r'custom-user', CustomUserViewSet)
router.register(r'jobrequest', JobRequestViewSet)
router.register(r'status-of-the-job-request', StatusOfTheJobRequestViewSet)
router.register(r'reporting', ReportingViewSet)
