from django import forms
from .models import VaPayroll


class PayrollCreateForm(forms.ModelForm):
    rate = forms.DecimalField(required=True)
    client = forms.CharField(required=True)

    class Meta:
        model = VaPayroll
        fields = ['date', 'virtual_assistant',
                  'time_in', 'time_out', 'client_name', 'rate']
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%y'), attrs={
                'class': 'form-control',
                'placeholder': 'Please select a date',
                'type': 'date',
            }),
            'time_in': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'time_out': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text'
            }),
            'rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'steps': '0.00'
            })
        }
