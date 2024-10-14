from django import forms
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'phone', 'email', 'dob', 'department','location',
            'emergency_contact', 'home_address', 'work_address', 'employee_type', 'travel_document', 'social_security'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
