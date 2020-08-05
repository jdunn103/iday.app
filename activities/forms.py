from django.forms import ModelForm, TextInput

from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name']
        widgets = {
            'name': TextInput(
                attrs={'autofocus': True, 'autocomplete': 'off'}
            )
        }
