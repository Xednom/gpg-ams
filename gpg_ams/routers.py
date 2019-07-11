from rest_framework import routers
from client.views import (
            ClientViewSet,
            ClientNameViewSet,
            ProjectManagerViewSet,
            TypeOfTaskViewSet,
            SeniorManagerViewSet,
            VirtualAssistantViewSet
        )
from users.views import (
    ClientViewSet, ClientCallMeViewSet, 
    StaffViewSet, VaViewSet, PmViewSet
    )
from landmaster.views import DueDiligenceViewSet, DueDiligenceTrackerViewSet

from jobrequest.views import JobRequestViewSet, JobRequestTitleViewSet
from reporting.views import ReportingViewSet
from logins.views import LoginsViewSet
from payroll.views import PayrollViewSet, PayrollCashOutViewSet
from clienttimesheet.views import TimeSheetViewSet, PaymentMadeViewSet
from reminders.views import ReminderViewSet
from callmeinventory.views import CallMeInventoryViewSet
from callmemasterboard.views import MasterBoardViewSets
from callmefinancialreport.views import FinancialViewSet
from marketingsites.views import InventoryViewSet
from landacademy.views import LandAcademyViewSet, SmartPricingViewSet

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
router.register(r'clients', ClientViewSet)
router.register(r'clients-callme', ClientCallMeViewSet, base_name="client")
router.register(r'staffs', StaffViewSet)
router.register(r'vas', VaViewSet, base_name="vas")
router.register(r'pms', PmViewSet, base_name="pms")
router.register(r'callme-inventory', CallMeInventoryViewSet, base_name='inventory')
router.register(r'callme-masterboard', MasterBoardViewSets, base_name='masterboard')
router.register(r'callme-financial-report', FinancialViewSet, base_name='financial')
router.register(r'marketing-sites', InventoryViewSet, base_name='marketing')
router.register(r'landacademy-inventory', LandAcademyViewSet, base_name='landacademy')
router.register(r'o2o-smart-pricing', SmartPricingViewSet, base_name='smartpricing')
