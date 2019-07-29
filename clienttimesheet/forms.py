from django import forms

from .models import TimeSheet


class TimeSheetCreateForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        exclude = ('assigned_pm',)

    def __init__(self, *args, **kwargs):
        self.assigned_pm = kwargs.pop('assigned_pm')
        super(TimeSheetCreateForm, self).__init__(*args, **kwargs)
