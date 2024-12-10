from django import forms
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


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
class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']