from rest_framework import routers
from client.views import (
            ClientViewSet,
            ClientNameViewSet,
            ProjectManagerViewSet,
            TypeOfTaskViewSet,
            SeniorManagerViewSet,
            VirtualAssistantViewSet
        )
from landmaster.views import DueDiligenceViewSet, DueDiligenceTrackerViewSet

from jobrequest.views import JobRequestViewSet, JobRequestTitleViewSet
from reporting.views import ReportingViewSet
from logins.views import LoginsViewSet
from payroll.views import PayrollViewSet, PayrollCashOutViewSet
from clienttimesheet.views import TimeSheetViewSet, PaymentMadeViewSet
from reminders.views import ReminderViewSet
from seller.views import (
    AffordableLandViewSet,
    FranklinManagementViewSet,
    )
from buyer.views import CustomerCareViewSet


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
router.register(r'due-diligence-tracker', DueDiligenceTrackerViewSet, base_name='DueDiligenceCleared')
router.register(r'logins', LoginsViewSet, base_name='Logins')
router.register(r'payroll', PayrollViewSet, base_name='Payroll')
router.register(r'cashout', PayrollCashOutViewSet, base_name='CashOut')
router.register(r'timesheet', TimeSheetViewSet, base_name='TimeSheet')
router.register(r'paymentmade', PaymentMadeViewSet, base_name='PaymentMade')
router.register(r'reminders', ReminderViewSet, base_name='ManagerReminders')
router.register(r'affordable-land', AffordableLandViewSet, base_name='affordableland')
router.register(r'franklin-management', FranklinManagementViewSet, base_name='franklinmanagement')
router.register(r'customer-care-specialist', CustomerCareViewSet, base_name='customercare')