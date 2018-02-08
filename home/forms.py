from django import forms
from home.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'desc',
        ]