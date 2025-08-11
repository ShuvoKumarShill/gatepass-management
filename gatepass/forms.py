from django import forms
from .models import GatePass

class GatePassForm(forms.ModelForm):
    class Meta:
        model = GatePass
        fields = [
            'visitor_name',
            'organization',
            'contact_number',
            'purpose',
            'date_of_entry',
            'time_of_entry',
            'approved_by',
            'status',
            'notes',
            'visitor_photo',
        ]
        widgets = {
            'date_of_entry': forms.DateInput(attrs={'type': 'date'}),
            'time_of_entry': forms.TimeInput(attrs={'type': 'time'}),
        }