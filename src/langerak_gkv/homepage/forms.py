from django import forms

from .models import PrayerOnDemand


class PrayerOnDemandForm(forms.ModelForm):
    class Meta:
        model = PrayerOnDemand
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        super(PrayerOnDemandForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'placeholder': field.label})
