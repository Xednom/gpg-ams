from rest_framework import routers
from client.views import (
            ClientViewSet,
            ClientNameViewSet,
            ProjectManagerViewSet,
            TypeOfTaskViewSet,
            SeniorManagerViewSet,
            VirtualAssistantViewSet
        )
from landmaster.views import DueDiligenceViewSet

from jobrequest.views import JobRequestViewSet, JobRequestTitleViewSet
from reporting.views import ReportingViewSet
from logins.views import LoginsViewSet
from payroll.views import PayrollViewSet


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet, base_name="Client")
router.register(r'client-name', ClientNameViewSet)
router.register(r'project-manager', ProjectManagerViewSet)
router.register(r'type-of-task', TypeOfTaskViewSet)
router.register(r'senior-manager', SeniorManagerViewSet)
router.register(r'virtual-assistant', VirtualAssistantViewSet)
router.register(r'jobrequest', JobRequestViewSet, base_name="JobRequest")
router.register(r'job-request-title', JobRequestTitleViewSet)
router.register(r'reporting', ReportingViewSet)
router.register(r'due-diligence', DueDiligenceViewSet, base_name='DueDiligence')
router.register(r'logins', LoginsViewSet, base_name='Logins')
router.register(r'payroll', PayrollViewSet, base_name='Payroll')