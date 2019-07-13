from django import forms

from .models import DueDiligencesCleared


class DueDiligenceCallCreateForm(forms.Form):
    date_of_call = forms.DateField(input_formats=['%d/%m/%Y'])
    call_in = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    call_out = forms.DateTimeField(input_formats=['%d/%m/%Y'])
