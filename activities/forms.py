from django import forms
from django.forms import ModelForm, TextInput

from .models import Activity, Event

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name']
        widgets = {
            'name': TextInput(
                attrs={'autofocus': True, 'autocomplete': 'off'}
            )
        }
        labels = {
            'name': 'Add an activity:'
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['activity']