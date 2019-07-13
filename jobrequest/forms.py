from django import forms

from .models import JobRequestTimeSheet


class JobRequestTimeSheetCreateForm(forms.Form):
    time_in = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    time_out = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
