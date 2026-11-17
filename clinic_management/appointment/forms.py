from django import forms
from .models import Appointment




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "patient_name",
            "patient_photo",
            "email",
            "phone",
            "appointment_date",
            "doctor",
            "reason",
        ]
        widgets = {
            "appointment_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
