from django import forms


class CalendarRangeForm(forms.Form):
    start = forms.DateField(localize=True)
    end = forms.DateField(localize=True)
