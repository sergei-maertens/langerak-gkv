from django import forms

from .models import PrayerOnDemand


class PrayerOnDemandForm(forms.ModelForm):
    class Meta:
        model = PrayerOnDemand
        fields = ('name', 'email', 'body')
