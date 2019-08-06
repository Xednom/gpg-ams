from django.contrib import admin
from .models import Client
from fillables.models import (
    InternalCompanyName,
    CompanyName,
    LeadSource,
    ProjectManager,
    SeniorManager,
    TypeOfTask,
    VirtualAssistant
    )

admin.site.register(InternalCompanyName)
admin.site.register(CompanyName)
admin.site.register(LeadSource)
admin.site.register(ProjectManager)
admin.site.register(SeniorManager)
admin.site.register(TypeOfTask)
admin.site.register(VirtualAssistant)
