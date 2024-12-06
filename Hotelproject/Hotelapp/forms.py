from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'checkin',
            'checkout',
            'adult_count',
            'child_count',
            'room_type',
            'special_request'
        ]

    # Add a custom widget for the date fields
    checkin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    checkout = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
