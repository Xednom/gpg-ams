from import_export import resources
from import_export.fields import Field

from .models import VaPayroll
from fillables.models import VirtualAssistant

class PayrollResource(resources.ModelResource):
    date = Field(attribute="date", column_name='Date')
    virtual_assistant = Field(attribute='virtual_assistant', column_name='Virtual Assistant')
    time_in = Field(attribute='time_in', column_name='Time In')
    time_out = Field(attribute='time_out', column_name='Time Out')
    hours = Field(attribute='hours', column_name='Total Hours')
    client_name = Field(attribute='client_name', column_name='Client Name')
    rate = Field(attribute='rate', column_name='Rate')
    salary = Field(attribute='salary', column_name='Salary')

    class Meta: 
        model = VaPayroll
        exclude = ('id',)
